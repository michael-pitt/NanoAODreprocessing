from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "W3Jets_MLM"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_mc.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/reNanoAOD/"
#config.Data.outLFNDirBase = "/store/group/cmst3/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "RunIISummer20UL17_NanoAODv9"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 15
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
