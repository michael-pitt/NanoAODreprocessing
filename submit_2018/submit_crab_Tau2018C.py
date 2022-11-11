from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "Tau_Run2018C-UL2018"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_data.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/Tau/Run2018C-UL2018_MiniAODv2-v1/MINIAOD" 
config.Data.outLFNDirBase = "/store/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "RunIISummer20UL18_NanoAODv9"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
