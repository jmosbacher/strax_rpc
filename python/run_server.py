if __name__ == '__main__':
    try:
        from straxrpc import StraxServer
        server = StraxServer()
        server.serve()
        
    except ImportError:
        print("failed to import straxrpc, is it installed?")

    except Exception as e:
        print(e)
