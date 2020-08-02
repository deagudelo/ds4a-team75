import dash
import dash_bootstrap_components as dbc
from ui import set_ui

external_scripts = [
    {
        'src': 'https://code.jquery.com/jquery-3.3.1.slim.min.js',
        'integrity': 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
        'integrity': 'sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
        'integrity': 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://kit.fontawesome.com/c96da4d2be.js',
        'crossorigin': 'anonymous'
    }

]
external_stylesheets = [
    {
        'rel': 'stylesheet',
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        'crossorigin': 'anonymous',
        'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'
    },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free-v4-shims.min.css',
        'media': 'all'
    },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free-v4-font-face.min.css',
        'media': 'all'
    },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free.min.css',
        'media': 'all'
    },
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    dbc.themes.BOOTSTRAP
]

application = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

server = application.server
application.config.suppress_callback_exceptions = True

set_ui(application)

if __name__ == '__main__':
    application.run_server(debug=True)  # , host='0.0.0.0', port=80)
    # app.run_server(host='0.0.0.0',port='8050',debug=True)
