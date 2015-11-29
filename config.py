config = {
    "debug": True,
    "flags_db": "flagsdb",
    "flag_regex": "\w{31}=",
    "worker_sleep_time": 1,
    "mongodb": {
        "host": "***REMOVED***",
        "port": 27017,
        "capped_collection_size": 5000
    },
    "flags_bulk_num": 80,
    "expireFlagAfter": 60*30

}
