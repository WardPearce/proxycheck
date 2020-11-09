class IpModel:
    def __init__(self, data: dict) -> None:
        self.asn = data["asn"] if "asn" in data else None
        self.provider = data["provider"] if "provider" in data else None
        self.continent = data["continent"] if "continent" in data else None
        self.country = data["country"] if "country" in data else None
        self.latitude = float(data["latitude"]) if "latitude" in data else None
        self.longitude = float(data["longitude"]) if "longitude" in \
            data else None
        self.isocode = data["isocode"] if "isocode" in data else None
        self.proxy = data["proxy"] == "yes" if "proxy" in data else None
        self.type = data["type"] if "type" in data else None
        self.risk = data["risk"] if "risk" in data else None
