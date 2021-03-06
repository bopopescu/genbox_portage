import elog_modules.mod_save, portage_exec, portage_exception

def process(mysettings, cpv, logentries, fulltext):
	elogfilename = elog_modules.mod_save.process(mysettings, cpv, logentries, fulltext)
	
	if not mysettings.get("PORTAGE_ELOG_COMMAND"):
		raise portage_exception.MissingParameter("!!! Custom logging requested but PORTAGE_ELOG_COMMAND is not defined")
	else:
		mylogcmd = mysettings["PORTAGE_ELOG_COMMAND"]
		mylogcmd = mylogcmd.replace("${LOGFILE}", elogfilename)
		mylogcmd = mylogcmd.replace("${PACKAGE}", cpv)
		retval = portage_exec.spawn_bash(mylogcmd)
		if retval != 0:
			raise portage_exception.PortageException("!!! PORTAGE_ELOG_COMMAND failed with exitcode %d" % retval)
	return
