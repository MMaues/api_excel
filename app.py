import pandas as pd
from flask import Flask, request, Response, send_file
from flask_restful import Resource, Api
from src.editorExcel import EditarExcel
import zipfile
import pathlib


app = Flask(__name__)
api = Api(app)

class app_main(Resource):

    @app.route("/v1/api/modificadorexcel", methods=["POST"])
    def modificar_excel(*self):
        response_excel: bytes = request.files["excel_notas"]
        notas_df: pd.DataFrame = pd.read_excel(response_excel)
        
        directory = pathlib.Path("files/")
        classe = EditarExcel()
        excel = classe.main(notas_df)
        
        with zipfile.ZipFile("notas.zip", mode="w") as archive:
            for file_path in directory.iterdir():
                archive.write(file_path, arcname=file_path.name)
                
        return send_file("notas.zip",as_attachment = True)
           
    
if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=2000)