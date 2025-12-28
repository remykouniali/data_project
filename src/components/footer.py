from dash import html

def create_footer():
    return html.Div([
        html.Div([
            html.Div([
                html.P([
                    "Data : ",
                    html.A(
                        "Open Data Football", 
                        href="https://github.com/openfootball", 
                        target="_blank",
                        className="footer-link"
                    )
                ], className="footer-text"),
                html.P([
                    "Projet multi-disciplinaire - ESIEE Paris"
                ], className="footer-text"),
            ], className="footer-content-left"),
            
            html.Div([
                html.P(["Dashboard"], className="footer-text footer-copyright")
            ], className="footer-content-right")
        ], className="footer-content")
    ], className="footer")
