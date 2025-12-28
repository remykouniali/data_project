from dash import html

def create_header():
    return html.Div([
        html.Div([
            html.Div([
                html.Span(className="header-icon"),
                html.H1("Dashboard Football Européen", className="header-title"),
            ], className="header-title-container"),
            html.P(
                "Analyse des performances des 5 grandes ligues européennes", 
                className="header-subtitle"
            ),
        ], className="header-content")
    ], className="header")
