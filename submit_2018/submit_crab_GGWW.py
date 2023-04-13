from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "GGToWW"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_mc.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/RunIISummer20UL18_GGToWW/cmst3-crab_GGToWW_mar9samples-c15273f0b6812ff053a850f456209388/USER" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/reNanoAOD/"
#config.Data.outLFNDirBase = "/store/group/cmst3/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "GGToWW"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 100
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
