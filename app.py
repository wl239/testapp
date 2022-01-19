from dash import *
from testapp import *
import dash_html_components as html

app = Dash(__name__)
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/tvol_banner.png")
])

if __name__ == '__main__':
    app.run_server(debug=True)
