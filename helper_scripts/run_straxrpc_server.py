if __name__ == '__main__':
    try:
        from straxrpc.server import StraxServer
        import strax
        server = StraxServer()
        st = strax.Context(register_all=strax.xenon.plugins,
                   storage=[
                        strax.DataDirectory('/home/mosbacher/custom_data', readonly=True),
                        # strax.SimpleS3Store(readonly=True),
                           ],
                   config={'pax_raw_dir' : './'}) # Does nothing
        st.register(strax.xenon.pax_interface.RecordsFromPax) 
        server.serve(st)
        
    except ImportError:
        print("failed to import straxrpc, is it installed?")

    except Exception as e:
        print(e)
