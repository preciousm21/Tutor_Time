#!/usr/bin/perl -w

# PREREQUISITE: make sure there are no line breaks inside cells
# You will get an error & know to fix if the course is of interest
# Hint: in course list, remove everything to the right of the rooms
# Whenever re-running student schedules, make sure to rerun course list as well
#	in Fall 2017, regitrar changed section letters between Aug & Sep!

# perl free_time.pl StudentsandCourses.SP18.1.5.18.csv CourseList.SP18.1.5.18.csv students/dh.txt
# perl free_time.pl CLA.StudentsandCourses.9.17.17.csv CLA.CourseList.9.17.17.csv ECON101 ECON102
# perl free_time.pl CLA.StudentsandCourses.9.17.17.csv Fall2017CourseList2.csv athletes/FH.csv
# No space in course name
# if you have spaces in your file names, need to be in quotes on the command line

# Before running the script the first time, please execute the following line in
# your terminal to install the Text::CSV module:
# 	sudo cpan Text::CSV
use Text::CSV;
my $csv = Text::CSV->new({ binary => 1, sep_char => ',' });

sub remove_trailing_newline {
    $_[0] =~ s/[\r\n]+\Z//;
  }

my $TEST = 0; # 0 for no extra output

my $student_schedules_file = shift @ARGV or die "Please enter a csv file\n";
my $course_list_file = shift @ARGV or die "Please enter a csv file\n";
# TODO crns could be just letters no numbers
# TODO crns could be file name of students
my %crns = ();
my %students = (); # list of students in target courses
for $crn (@ARGV) {
	if ($crn =~ /\.csv$/) {
		open(IN, $crn) or die "Couldn't read input file $crn: $!\n";
		my $group = $crn;
		$group =~ s/(\S+\/)*(\S+)\.csv/$2/;
		while (my $line = <IN>) {
			#chomp $line;
			remove_trailing_newline($line);
			my @list = split(',', $line);
			my $id = $list[0];
			my $name = $list[1];
			$crns{$group} = 1;
			$students{$name} = 0; # What if we don't find student?
			#print "$group - $name - $line\n";
		}
		close IN;
	} elsif ($crn =~ /\.txt$/) {
		open(IN, $crn) or die "Couldn't read input file $crn: $!\n";
		my $group = $crn;
		$group =~ s/(\S+\/)*(\S+)\.txt/$2/;
		while (my $line = <IN>) {
			#chomp $line;
			remove_trailing_newline($line);
			$crns{$group} = 1;
			$students{$line} = 0; # What if we don't find student?
			#print "$group - $name - $line\n";
		}
		close IN;
	} else {
		$crns{$crn} = 1;
	}
}

if ($TEST) {
	print "CRNS: ";
	for my $crn (sort keys %crns) {
		print "$crn ";
	}
	print "\n";
}

my $outfile = "busy_".join("_", sort keys %crns)."-students.txt";
my $outsched = "busy_".join("_", sort keys %crns)."-schedule.txt";
#my $crn = shift @ARGV;
#print($student_schedules_file."\n");
my %courses = (); # course-section -> time blocks -> days of week
my %times = (); # hashmap of students -> sections instead of matrix
my %all_sections = ();
my @all_days = ("M", "T", "W", "R", "F");
my %course_times = (); # course-section -> string time

open(TESTING, ">test.txt") or die "Testing\n" if ($TEST == 1);

sub update_times($$$$) {
	my ($student, $course, $num, $section) = @_;
	#my @sections = split(//, $section);
	# get sections from courses now by
	my $section_name = "$course$num-$section";
	# for each time block
	print(TESTING "$student: ".$course_times{"$course$num-$section"}."\n") if ($TEST == 1) and defined($course_times{"$course$num-$section"});
	for $time (keys %{$courses{$section_name}}) {
		# for each day
		for $day (keys %{$courses{$section_name}{$time}}) {
			print(TESTING "\t$section_name $time $day\n") if ($TEST == 1);
			$times{$student}{$time}{$day} = "$course$num";
		}
		$all_sections{$time} = 1;
	}
}

open(FILE, $course_list_file) or die "Couldn't read input file $course_list_file: $!\n";
while (my $line = <FILE>) {
	next if $line =~ /Seats\s+Available/;
	if ($csv->parse($line)) {
		#my @list = split(/,/, $line);
		my @list = $csv->fields();
		my $course = $list[3];
		my $num = $list[4];
		$num = "001" if ($num eq "1");
		my $section = $list[5];
		# my $crn = $list[6];
		my $time = $list[19];
		$course_times{"$course$num-$section"} = $time;
		my @times = split(/;\s*/, $time);
		for $t (@times) {
			# day(s) start: hour min am end: hour min am
			if ($t =~ /^\s*([MTWRF]+)\s+(\d+):(\d+)\s+([AP]M)\s*-\s*(\d+):(\d+)\s+([AP]M)\s*$/) {
				my @days = split(//, $1);
				my $s_h = int($2);
				my $s_m = int(int($3) / 15) * 15;
				my $s_am = $4;
				my $e_h = int($5);
				my $e_m = (int(int($6) / 15) + 1) * 15;
				my $e_am = $7;
				print(TESTING "$course$num-$section @days $s_h : $s_m -- $e_h : $e_m\n") if ($TEST == 1);
				$s_am = "NN" if ($s_h == 12);
				$e_am = "NN" if ($e_h == 12);
				my $hour = $s_h;
				my $hour24 = $s_h;
				$hour24 += 12 if ($s_am eq "PM");
				$e_h += 12 if ($e_am eq "PM");
				my $min  = $s_m;
				my $am   = $s_am;
				while ($hour24 <= $e_h) {
					print(TESTING "\tWHILE $hour24 <= $e_h $hour : $min $am\n") if ($TEST == 1);
					if ($hour24 == $e_h and $min >= $e_m) {
						$hour24 += 1; # break
					} else {
						# add time block
						my $m = $min;
						$m = "00" if ($min == "0");
						my $h = $hour;
						$h = "0" . $hour if ($hour < 10);
						for $d (@days) {
							$courses{"$course$num-$section"}{"$am $h:$m"}{$d} = 1;
						}
						#print(TESTING "\t$course$num-$section $am $hour:$min @days\n") if ($TEST == 1);
						$min += 15;
						if ($min == 60) {
							$min = 0;
							$hour += 1;
							$hour24 += 1;
							if ($hour == 12) {
								$am = "NN";
							} elsif ($hour == 13) {
								$hour = 1;
								$am = "PM";
							}
						}
					}
				}
			} elsif ($t !~ /^\s*([MTWRF]+)?\s*-?\s*$/) {
				print(TESTING "ERROR $course$num-$section: $t\n") if ($TEST == 1);
				warn "Couldn't parse time for $course$num-$section: $t\n";
			}
		}
	} else {
		warn "Line could not be parsed: ".$csv->error_diag()."\n\t$line\n";
	}
}
close FILE;

open(FILE, $student_schedules_file) or die "Couldn't read input file $student_schedules_file: $!\n";
my $student = "FIX ME";
while (my $line = <FILE>) {
	# find first line of each record to get student
	my @list = split(/,/, $line);
	if ($line =~ /student\s+type/i) {	
		$student = $list[1];
		$students{$student}++ if (defined $students{$student} and $students{$student} == 0);
		print(TESTING "--$student--\n") if ($TEST == 1);
	} elsif ($line !~ /^(\s+-\s+)?,+\s*$/ and $line !~ /^\s*$/ and $line !~ /Total\s+For/ and $line !~ /Course\s+Title/) {
		print(TESTING $list[0]) if ($TEST == 1);
		# get course data
		if ($list[0] =~ /(\w+)\s+(\w+)\s+-\s+(\w+)/) {
			print(TESTING "---in---") if ($TEST == 1);
			my $course = $1;
			my $num = $2;
			my $section = $3;
			my $curr_crn = "$course$num";
			if (defined $crns{$curr_crn} or defined $crns{$course}) {
				$students{$student} = 1;
			}
			update_times($student, $course, $num, $section);
		}
		print(TESTING "\n") if ($TEST == 1);
	} 
}
close FILE;

for $student (sort keys %students) {
	print("ERROR: $student not found in schedule\n") if ($students{$student} == 0);
}

#exit() if ($TEST == 1);

open(SCHED, ">$outsched") or die "ERROR couldn't open $outsched: $!\n";	

# TODO: CHEM 150 should have 100% busy MWF @ 9:10-10:15!!
my $num_students = scalar(keys %students);
if ($num_students > 0) {
	
	# Print out time by day grid of busiest slots
	print(SCHED "Busy times for ".(join(", ", sort keys %crns))." ($num_students enrolled):\n");
	printf(SCHED "%8s\t", " ");
	for $day (@all_days) {
		printf(SCHED "%10s\t", $day);
	}
	print(SCHED "\n");
	for $section (sort keys %all_sections) {
		printf(SCHED "%8s\t", $section);
		for $day (@all_days) {
			my $busy = 0;
			for $student (sort keys %students) {
				if (defined $times{$student} and defined $times{$student}{$section} and defined $times{$student}{$section}{$day}) {
					$busy += 1;
				}
			}
			my $percent = int(100 * $busy / $num_students);
			printf(SCHED "%5d (%3d %s)\t", $busy, $percent, "%");
		}
		print(SCHED "\n");
	}

	# Print out all busy students by day-time
	open(OUT, ">$outfile") or print "ERROR couldn't open $outfile: $!\n";	
	print(OUT "Busy students by time slot:\n");
	for $day (@all_days) {
		for $section (sort keys %all_sections) {
			print(OUT "$day $section: \n");
			for $student (sort keys %students) {
				if (defined $times{$student} and defined $times{$student}{$section} and defined $times{$student}{$section}{$day}) {
					my $format = sprintf("%40s %10s\n", $student, $times{$student}{$section}{$day});
					print(OUT "$format");
				}
			}
			print(OUT "\n");
		}
	}
	close OUT;
} else {
	print("ERROR: BAD COURSE OR COURSE(S) HAVE NO STUDENTS\n");
}

close OUT;
close SCHED;
close TESTING if ($TEST == 1);

open(IN, "$outsched");
while(<IN>) {
	print;
}
close IN;