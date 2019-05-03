if {[catch {package present Tcl 8.5.0}]} { return }
<<<<<<< HEAD
package ifneeded Tk 8.5.9	[list load [file join $dir .. .. Tk] Tk]
=======
if {($::tcl_platform(platform) eq "unix") && ([info exists ::env(DISPLAY)]
	|| ([info exists ::argv] && ("-display" in $::argv)))} {
    package ifneeded Tk 8.5.15 [list load [file join $dir .. .. bin libtk8.5.dll] Tk]
} else {
    package ifneeded Tk 8.5.15 [list load [file join $dir .. .. bin tk85.dll] Tk]
}
>>>>>>> 570e0bbcb5c32d03229a0c27839d62befc3fd00e
