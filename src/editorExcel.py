import pandas as pd
import os

class EditarExcel():
    def main(self, notas_df: pd.DataFrame):
        
        file_path: str = os.getcwd()+"/files"
        nomes_professores = notas_df.drop_duplicates(subset=["Professor"], keep="first")
        nomes_professores = list(nomes_professores["Professor"])
        
        for professor in nomes_professores:
            professor_df: pd.DataFrame = self.separar_df(notas_df, professor)
            excel_notas = professor_df.to_excel('{}\{}'.format(file_path,professor+".xlsx"), sheet_name='Planilha1', index=False)
        
        return excel_notas

    def separar_df(self, notas_df: pd.DataFrame, nome: str):
        df = notas_df.drop(notas_df.index[notas_df["Professor"] != nome ])
        return df