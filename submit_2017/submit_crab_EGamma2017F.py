from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "SingleElectron_Run2017F"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_data.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/reNanoAOD/"
config.Data.outputDatasetTag = "SingleElectron_Run2017F-RunIISummer20UL17_NanoAODv9"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
