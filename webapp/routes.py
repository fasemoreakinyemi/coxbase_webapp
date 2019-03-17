def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=1)
    config.add_route('home', '/')
    config.add_route('search_results', '/result/{item}')
    config.add_route('No_entry', '/result/noentry/{item}')
    config.add_route('search_page', '/result')
    config.add_route('detailed_view', '/result/details/{uid}')
    config.add_route('wiki_view', '/wiki')
    config.add_route('wikipage_add', '/wiki/add')
    config.add_route('wikipage_view', '/wiki/{uid}')
    config.add_route('wikipage_edit', '/wiki/{uid}/edit')
    config.add_route('api', '/api')
    config.add_route('api_filter', '/api/{column}/{filter}/{filter_value}')
    config.add_route('api_column', '/api/{column}')
    config.add_route('api2', '/api2')
    config.add_route('seek_species', '/api2/{id}')
    config.add_route('search', '/search')
    config.add_route('dashboard', '/dashboard')
    config.add_route('dashboard_new', '/dashboard/{path}')
    config.add_route('api_map', '/api_map/{column}/{state}')

