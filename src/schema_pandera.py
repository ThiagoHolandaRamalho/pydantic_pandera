import pandera as pa
from pandera.typing import DataFrame, Series
from datetime import datetime



class SchemaCorpApolice(pa.SchemaModel):
    """
    Esquema de validação para DataFrames relacionados a apólices corporativas.

    Esta classe valida os dados de apólices corporativas, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes: 
        cd_apolice (Series[int]): Código identificador da apólice (obrigatório).
        nm_produto (Series[str]): Nome do produto associado à apólice (obrigatório).
        quantidade (Series[int]): Quantidade de itens associados à apólice (≥ 0).
        valor (Series[float]): Valor monetário associado à apólice (≥ 0.0).
        dt_emissao (Series[datetime]): Data de emissão da apólice (obrigatório).
        dv_documento_oficial (Series[bool]): Indicador se há documento oficial válido.
    """

    cd_apolice: Series[int] = pa.Field(ge=1, description="Código da apólice (≥ 1)")
    nm_produto: Series[str] = pa.Field(nullable=False, description="Nome do produto")
    quantidade: Series[int] = pa.Field(ge=0, description="Quantidade de itens (≥ 0)")
    valor: Series[float] = pa.Field(ge=0.0, description="Valor da apólice (≥ 0.0)")
    dt_emissao: Series[datetime] = pa.Field(description="Data de emissão da apólice")
    dv_documento_oficial: Series[bool] = pa.Field(description="Documento oficial válido (True/False)")

    class Config:
        """
        Configurações adicionais do esquema.

        Attributes:
            coerce (bool): Converte automaticamente os tipos de dados.
            strict (bool): Garante que apenas as colunas definidas são aceitas.
        """
        coerce = True  # Força a conversão para os tipos definidos no esquema
        strict = True  # Apenas aceita colunas explicitamente definidas no esquema

    @staticmethod
    def validar(df: DataFrame) -> DataFrame: 
        """
        Valida um DataFrame conforme o esquema definido.

        Args:
            df (DataFrame): DataFrame a ser validado.

        Returns:
            DataFrame: DataFrame validado.

        Raises:
            pa.errors.SchemaError: Se os dados não atenderem aos requisitos do esquema.
        """
        return SchemaCorpApolice.validate(df)
