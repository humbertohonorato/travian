URL_BASE_SERVER = "https://lusobr.x1.lusobrasileiro.travian.com"

API_VERSION = "api/v1"
API_TILE_DETAILS_PATH = "map/tile-details"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
CONTENT_TYPE = 'application/json; charset=UTF-8'
ACCECPT = "application/json, text/javascript, */*; q=0.01"

BEARER_TOKEN = "Bearer 7e2ac00d32eb5aac7b3b9a5e"
COOKIE = "__cmpconsentx17155=CPw6W7gPw6W7gAfSDBPTDTCgAP_AAH_AAAYgfstf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsb02cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7______7_______________________________________________________________________-___AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYfstf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsb02cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7______7_______________________________________________________________________-___AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAA; __cmpcccx17155=aBPw7prfgAwAzADcEGAAIABwAGAAeABQAGAAOAAnABcAGAANQAdAB6AEAARQAkACUAFAALgAYgA0AB5AEAAQQAmgBeAD2AIcAYgBBQCFgEaAI6ATgAp4BVwDKgGhAOYAuMBugDfQHBAOJAeWA9ECDgENgIkgRMAigBMACZYFPALAgWZAtEBb0C4IFwwM1AZ4A68CHQERAI3wSMAkvBMECY6E3gTegoUBRoAMF1UL4oZWQ6ZpYSURUA; _ga_QQZEB4FZFX=GS1.2.1692750704.2.1.1692750851.0.0.0; _ga=GA1.1.78727607.1692706946; _pbjs_userid_consent_data=3524755945110770; _cc_id=e74766160e0ef1542a2523eb8a2c3156; _ga_ZQMM0SFYTB=GS1.1.1695315480.4.1.1695316153.0.0.0; panoramaId_expiry=1696628068039; panoramaId=8b23865d588232eed3cd1b59c51216d5393845846a112305e7030adc99b7e736; cto_bidid=cupLsl9QeDQyMDdjVVBaa09UeDUwZGU2ZThNd0VFZVBSMzhidGg0V0VxYyUyRlRUVzlJUXBkeXl1Q3hBQnNZa3VwOSUyRnYlMkJGOXk0WHZ4UFpBMGhnejR1R1BjRmtzbTFwMkZQSGl1VG9JQ0VwYVdWS29xcyUzRA; cto_dna_bundle=w5_9mV80M0RITmhlJTJCZkMwOUJGQlhaMUN2czNuZGtOcEUlMkZQRVFaSGdGMVpSVUxCYnBNOEh5ZWd4a2xzZmlRNzhGU1BxYQ; cto_bundle=vm0CQF9WM1diQUI2ZTJNbTFtWnNjVmlKOHNFMFlTNFBRTmVHdlZ4T21jeWN4QyUyRmRvN09TcE9tZFBrSjg5RERQc2FYcVVnY1dJQXlSRmhBVkxveWdTZEgxTTVhQkZSb0VZJTJGOXhpMkc0MnpJdE0wUWxvbDNSTElRbjJqbVJwbTBlODV1Y2YxTURkOFVmc1JFUXNEUFBQd0tIWjRnJTNEJTNE; __gads=ID=43d1fb823386cb8c:T=1694116322:RT=1696592645:S=ALNI_MaRGWqD-l7zoNAXh21-oFK6iYf7aA; JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhTmc0NWFRUDNFcUJ0NmRQWTNxMWtWTXEyV1N0dGJKTyIsImF1ZCI6ImU0NjhjMDAwLTQwYzEtMTFlZS0xYTAxLTAwMDAwMDAwMDAwMCIsImV4cCI6MTY5NjYxOTYyNSwicHJvcGVydGllcyI6eyJoYXNoIjoiNzk2MDZjMTBjNGIwNzk2MFB0eVRzRWJMVUFWODRnbUkiLCJtb2JpbGVPcHRpbWl6YXRpb25zIjpmYWxzZSwibG9naW5JZCI6NTM3OTIyLCJsYW5ndWFnZSI6InB0LVBUIiwidmlsbGFnZVBlcnNwZWN0aXZlIjoicGVyc3BlY3RpdmVSZXNvdXJjZXMiLCJwdyI6IkZtcXFxYXd5T0dMT0VESzJsNkUyVTUxbHlFZHNyYWY5IiwiZGlkIjoyNTgyMn19.j74CjfYJWDl2xeKgAMgbXsaBBoASMBdKVGf-caiJjJ47wKDym1F1gd49rqsHfoFEFh5Eerp77OIhAiDOqOqk156jZnq7vLwgi1ii7DhTiAMtp4gKGQDkNK4OFqWt0d7ndkqNUVQNHTpuhEm2d9q4n1rH6mixcU2D6YXXLfYXcqtKstG8PqhuMY_PIJ183YxGmstIjmZe_--IasLlQtkQROvak8C7zT5noJ-8Q4-8SwNvW0zCKVpAxD95YEdwafNST2VRAlREHHsXW8DcVXyLgLkqhyxjOmUzlj04LvQQ9CI_EYeLXsryMBXksRYF9al8TvwbJTStWMCVwPkYh_gJXg"

COORD_X = 60
COORD_Y = -6
