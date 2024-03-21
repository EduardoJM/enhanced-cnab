from cnab.base.retorno.CNAB400 import Registro9Retorno
from cnab.core.field import CNABField, CNABFieldType


class BradescoRetornoCnab400Registro9(Registro9Retorno):
    _meta = {
        "tipo_registro": CNABField(  # 01.5
            length=1, default="9", validation=CNABFieldType.Int, required=True
        ),
        "ident_retorno": CNABField(  # 01.5
            length=1, default="2", validation=CNABFieldType.Int, required=True
        ),
        "ident__tipo_retorno": CNABField(  # 01.5
            length=2, default="01", validation=CNABFieldType.Int, required=True
        ),
        "codigo_banco": CNABField(  # 01.5
            length=3, default="237", validation=CNABFieldType.Int, required=True
        ),
        "filler0": CNABField(  # 02.5
            length=10, default="", validation=CNABFieldType.Alfa, required=True
        ),
        "qtd_titulos_cobranca": CNABField(  # 03.5
            length=8, default="1", validation=CNABFieldType.Int, required=True
        ),
        "valor_total_cobranca": CNABField(  # 04.5
            length=12,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "n_aviso_bancario": CNABField(  # 05.5
            length=8, default="1", validation=CNABFieldType.Alfa, required=True
        ),
        "filler1": CNABField(  # 06.5
            length=10, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "QtdEntradaConfirmadaC02": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValEntradaConfirmadaC02": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "ValTotLiquidacaoC06": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdLiquidacaoC06": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValLiquidacaoC06": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdBaixaC09C10": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValBaixaC09C10": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdAbatimentoCanceladoC13": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValAbatimentoCanceladoC13": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdVencimentoAlteradoC14": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValVencimentoAlteradoC14": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdAbatimentoConcedidoC12": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValAbatimentoConcedidoC12": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdConfirmacaoInstProtestoC19": CNABField(  # 12.5
            length=5, default="", validation=CNABFieldType.Int, required=True
        ),
        "ValConfirmacaoInstProtestoC19": CNABField(  # 04.5
            length=10,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "filler2": CNABField(  # 06.5
            length=174, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "ValTotalRateiosEfetuados": CNABField(  # 04.5
            length=13,
            default="",
            validation=CNABFieldType.Decimal,
            precision=2,
            required=True,
        ),
        "QtdTotalRateiosEfetuados": CNABField(  # 12.5
            length=8, default="", validation=CNABFieldType.Int, required=True
        ),
        "filler3": CNABField(  # 06.5
            length=9, default=" ", validation=CNABFieldType.Alfa, required=True
        ),
        "numero_sequencial_registro": CNABField(
            length=6, default="", validation=CNABFieldType.Int, required=True
        ),
    }
