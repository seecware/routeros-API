from fastapi import APIRouter
from utils.mikrotik import get_api

router = APIRouter()

@router.get("/interfaces")
def get_interfaces():
    try:
        api = get_api()
        interfaces = list(api.path("interface"))
        return {"interfaces": interfaces}
    except Exception as e:
        return {"error": str(e)}

@router.get("/leases")
def get_all_leases():
    try:
        api = get_api()
        leases = list(api.path("ip", "dhcp-server", "lease"))
        return {"leases": leases}
    except Exception as e:
        return {"error": str(e)}
