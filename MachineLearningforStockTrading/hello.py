from nameko.rpc import rpc

class GreetingService:
    name = "greeting_service"

    @rpc
    def get_olhc(self):
        
        
        return oanda_data