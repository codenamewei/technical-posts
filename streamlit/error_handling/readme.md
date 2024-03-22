# Error Handling Strategy with Streamlit and FastAPI Implementation

Effective capturing and displaying of error messages with the Streamlit and FastAPI stack

<img src="public/banner.png">


## Run it locally with Docker
```
chmod +x build-script.sh
./build-script.sh
```

## To run it without Docker

### Backend
```
uvicorn backend:app
```

### Frontend
- Before booting up Streamlit application, change _line 14_ in **frontend.py** from   
`server_url = "http://sample-app-backend:8000/"`  
to  
`server_url = "http://localhost:8000/"`

```
streamlit run frontend.py
```


### Streamlit configuration to hide the side bar 

Add below to .streamlit/config.toml
```
# Controls whether the default sidebar page navigation in a multipage app is
# displayed.
# Default: true
showSidebarNavigation = false
```
- Read more about config.toml in [docs](https://docs.streamlit.io/library/advanced-features/configuration#client)

