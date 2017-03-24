session-get

//--req
{
	"method": "session-get"
}


//--res

{
	"arguments": {
		"alt-speed-down": 50,
		"alt-speed-enabled": false,
		"alt-speed-time-begin": 540,
		"alt-speed-time-day": 127,
		"alt-speed-time-enabled": false,
		"alt-speed-time-end": 1020,
		"alt-speed-up": 50,
		"blocklist-enabled": false,
		"blocklist-size": 0,
		"blocklist-url": "http://www.example.com/blocklist",
		"cache-size-mb": 4,
		"config-dir": "/home/likemilk/.config/transmission",
		"dht-enabled": true,
		"download-dir": "/home/likemilk/\ub2e4\uc6b4\ub85c\ub4dc",
		"download-dir-free-space": 7919644672,
		"download-queue-enabled": true,
		"download-queue-size": 5,
		"encryption": "preferred",
		"idle-seeding-limit": 30,
		"idle-seeding-limit-enabled": false,
		"incomplete-dir": "/home/likemilk/\ub2e4\uc6b4\ub85c\ub4dc",
		"incomplete-dir-enabled": false,
		"lpd-enabled": false,
		"peer-limit-global": 200,
		"peer-limit-per-torrent": 50,
		"peer-port": 51413,
		"peer-port-random-on-start": false,
		"pex-enabled": true,
		"port-forwarding-enabled": true,
		"queue-stalled-enabled": true,
		"queue-stalled-minutes": 30,
		"rename-partial-files": true,
		"rpc-version": 15,
		"rpc-version-minimum": 1,
		"script-torrent-done-enabled": false,
		"script-torrent-done-filename": "/home/likemilk",
		"seed-queue-enabled": false,
		"seed-queue-size": 10,
		"seedRatioLimit": 2,
		"seedRatioLimited": false,
		"speed-limit-down": 100,
		"speed-limit-down-enabled": false,
		"speed-limit-up": 100,
		"speed-limit-up-enabled": false,
		"start-added-torrents": true,
		"trash-original-torrent-files": false,
		"units": {
			"memory-bytes": 1024,
			"memory-units": ["KiB", "MiB", "GiB", "TiB"],
			"size-bytes": 1000,
			"size-units": ["kB", "MB", "GB", "TB"],
			"speed-bytes": 1000,
			"speed-units": ["kB/\ucd08", "MB/\ucd08", "GB/\ucd08", "TB/\ucd08"]
		},
		"utp-enabled": true,
		"version": "2.84 (14307)"
	},
	"result": "success"
}


torrent-get

//--req
{
	"method": "torrent-get",
	"arguments": {
		"fields": ["id","error" "name", "errorString", "percentDone", "files", "sizeWhenDone", "queuePosition", "rateDownload", "rateUpload", "recheckProgress", "seedRatioMode", "seedRatioLimit", "status", "trackers", "downloadDir", "uploadedEver", "uploadRatio", "webseedsSendingToUs"],
		"ids": [1,2,3,4, ....... 99,100]
	}
}

//--res
{
	"arguments": {
		"removed": [],
		"torrents": [{
			"downloadDir": "/home/likemilk/\ub2e4\uc6b4\ub85c\ub4dc",
			"error": 0,
			"errorString": "",
			"eta": -2,
			"id": 1,
			"isFinished": false,
			"isStalled": false,
			"leftUntilDone": 304545792,
			"metadataPercentComplete": 1,
			"peersConnected": 1,
			"peersGettingFromUs": 0,
			"peersSendingToUs": 0,
			"percentDone": 0.0801,
			"queuePosition": 0,
			"rateDownload": 0,
			"rateUpload": 0,
			"recheckProgress": 0,
			"seedRatioLimit": 2,
			"seedRatioMode": 0,
			"sizeWhenDone": 331088130,
			"status": 4,
      "name": "{~~~~~~~~~~~~~~}"
      "files": [
        {
          "bytesCompleted": 88328699
          ,"length": 268683771
          "name": "[Leopard-Raws] Boku dake ga Inai Machi (CX 1280x720 x264 AAC)/[Leopard-Raws] Boku dake ga Inai Machi - 08 RAW (CX 1280x720 x264 AAC).mp4"
        }
      ],
			"trackers": [{
				"announce": "udp://a.leopard-raws.org:6969/announce",
				"id": 0,
				"scrape": "udp://a.leopard-raws.org:6969/scrape",
				"tier": 0
			}, {
				"announce": "udp://tracker.openbittorrent.com:80/announce",
				"id": 1,
				"scrape": "udp://tracker.openbittorrent.com:80/scrape",
				"tier": 1
			}, {
				"announce": "udp://tracker.publicbt.com:80/announce",
				"id": 2,
				"scrape": "udp://tracker.publicbt.com:80/scrape",
				"tier": 2
			}, {
				"announce": "http://open.nyaatorrents.info:6544/announce",
				"id": 3,
				"scrape": "http://open.nyaatorrents.info:6544/scrape",
				"tier": 3
			}],
			"uploadRatio": 0,
			"uploadedEver": 0,
			"webseedsSendingToUs": 0
		}]
	},
	"result": "success"
}

session-stats

//--req
{
	"method": "session-stats"
}

//--res
{
	"arguments": {
		"activeTorrentCount": 1,
		"cumulative-stats": {
			"downloadedBytes": 577616401,
			"filesAdded": 8,
			"secondsActive": 175643,
			"sessionCount": 7,
			"uploadedBytes": 85641558
		},
		"current-stats": {
			"downloadedBytes": 1095444,
			"filesAdded": 1,
			"secondsActive": 3482,
			"sessionCount": 1,
			"uploadedBytes": 0
		},
		"downloadSpeed": 0,
		"pausedTorrentCount": 0,
		"torrentCount": 1,
		"uploadSpeed": 0
	},
	"result": "success"
}


free-space

//--req
{
	"method": "free-space",
	"arguments": {
		"path": "/home/likemilk/다운로드"
	}
}

//--res
{
	"arguments": {
		"path": "/home/likemilk/\ub2e4\uc6b4\ub85c\ub4dc",
		"size-bytes": 7919644672
	},
	"result": "success"
}


torrent-add

//--req
{
	"method": "torrent-add",
	"arguments": {
		"paused": false,
		"download-dir": "/home/likemilk/다운로드",
		"metainfo": "${payload}"
	}
}

//--res
{
	"arguments": {
		"torrent-added": {
			"hashString": "1b092065c083762c01d16ca788f35d4b8b996613",
			"id": 2,
			"name": "[Leopard-Raws] Boku dake ga Inai Machi (CX 1280x720 x264 AAC)"
		}
	},
	"result": "success"
}


torrent-remove

//--req
{
	"method": "torrent-remove",
	"arguments": {
		"ids": [2]
	}
}

//--res
{
	"arguments": {},
	"result": "success"
}

torrent-stop

//req
{
	"method": "torrent-stop",
	"arguments": {
		"ids": [1]
	}
}

//res
{
	"arguments": {},
	"result": "success"
}
