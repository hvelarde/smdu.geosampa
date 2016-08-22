# -*- coding: utf-8 -*-
"""Formulário de cadastro de Parklet."""
from plone.autoform import directives as form
from plone.autoform.form import AutoExtensibleForm
from plone.formwidget.geolocation.field import GeolocationField
from plone.namedfile.field import NamedFile
from plone.supermodel import model
from smdu.geosampa import _
from z3c.form import button
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.form import EditForm
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

vocabulary_1 = SimpleVocabulary([
    SimpleTerm(value=u'11', title=_(u'Residencial Horizontal')),
    SimpleTerm(value=u'12', title=_(u'Residencial Vertical')),
    SimpleTerm(value=u'13', title=_(u'Comercial Varejo')),
    SimpleTerm(value=u'14', title=_(u'Restaurante ou bar')),
    SimpleTerm(value=u'15', title=_(u'Serviço Saúde')),
    SimpleTerm(value=u'16', title=_(u'Serviço Educacional')),
    SimpleTerm(value=u'17', title=_(u'Industrial')),
    SimpleTerm(value=u'18', title=_(u'Outros')),
])

vocabulary_2 = SimpleVocabulary([
    SimpleTerm(value=u'21', title=_(u'Madeira')),
    SimpleTerm(value=u'22', title=_(u'Aço')),
    SimpleTerm(value=u'23', title=_(u'Piso cimentício')),
    SimpleTerm(value=u'24', title=_(u'Metálico')),
    SimpleTerm(value=u'25', title=_(u'Plástico')),
])


class IParklet(model.Schema):

    """Form fields."""

    model.fieldset(
        'tab_a',
        label=_(u'Local de implantação'),
        fields=['cep', 'address_1', 'address_2', 'address_3', 'geolocation'],
    )

    cep = schema.ASCIILine(
        title=_(u'CEP'),
    )

    address_1 = schema.TextLine(
        title=_(u'Address 1'),
    )

    address_2 = schema.TextLine(
        title=_(u'Address 2'),
    )

    address_3 = schema.TextLine(
        title=_(u'Address 3'),
    )

    geolocation = GeolocationField(
        title=_('label_geolocation', default=u'Geolocation'),
        description=_(
            'help_geolocation',
            default=u'Click on the map to select a location, or use the text input to search by address.'),
        required=False
    )

    model.fieldset(
        'tab_b',
        label=_(u'Características do local'),
        fields=[
            'field_1',
            'field_2',
            'field_3',
            'field_4',
            'field_5',
            'field_6',
            'field_7',
            'field_8',
            'field_9',
            'field_10',
            'field_11',
            'field_12',
            'field_13',
            'field_14',
            'field_15',
            'field_16',
            'field_17',
            'field_18',
            'field_19',
        ],
    )

    form.widget('field_1', RadioFieldWidget)
    field_1 = schema.Bool(
        title=_(u'Vaga permanente de estacionamento (24 horas por dia)'),
    )

    form.widget('field_2', RadioFieldWidget)
    field_2 = schema.Bool(
        title=_(u'Velocidade da via é igual ou inferior a 50km/h'),
    )

    form.widget('field_3', RadioFieldWidget)
    field_3 = schema.Bool(
        title=_(u'Distância de 15m do bordo do alinhamento da rua transversal'),
    )

    form.widget('field_4', RadioFieldWidget)
    field_4 = schema.Bool(
        title=_(u'A declividade longitudinal da rua inferior a 8,33%'),
    )

    form.widget('field_5', RadioFieldWidget)
    field_5 = schema.Bool(
        title=_(u'Rua com histórico de alagamentos e enxurradas'),
    )

    form.widget('field_6', RadioFieldWidget)
    field_6 = schema.Bool(
        title=_(u'Calçada em bom estado de conservação'),
    )

    form.widget('field_7', RadioFieldWidget)
    field_7 = schema.Bool(
        title=_(u'Obstrui faixa de pedestre'),
    )

    field_8 = schema.Text(
        title=_(u'Justificativa'),
    )

    form.widget('field_9', RadioFieldWidget)
    field_9 = schema.Bool(
        title=_(u'Obstrui vagas especiais de estacionamento'),
    )

    form.widget('field_10', RadioFieldWidget)
    field_10 = schema.Bool(
        title=_(u'Obstrui guias rebaixadas'),
    )

    form.widget('field_11', RadioFieldWidget)
    field_11 = schema.Bool(
        title=_(u'Defronte à saída de água pluvial'),
    )

    form.widget('field_12', RadioFieldWidget)
    field_12 = schema.Bool(
        title=_(u'Obstrui boca-de-lobo/bueiro'),
    )

    field_13 = schema.Text(
        title=_(u'Descreva'),
    )

    field_14 = schema.TextLine(
        title=_(u'Largura da calçada (em metros)'),
    )

    field_15 = schema.TextLine(
        title=_(u'Porcentagem da área sombreada no trecho do parklet a ser implantado'),
    )

    form.widget('field_16', RadioFieldWidget)
    field_16 = schema.Bool(
        title=_(u'Já possui mobiliário urbano?'),
    )

    field_17 = schema.TextLine(
        title=_(u'De que tipo?'),
    )

    form.widget('field_18', RadioFieldWidget)
    field_18 = schema.Bool(
        title=_(u'O proponente é proprietário do imóvel?'),
    )

    field_19 = schema.Choice(
        title=_(u'Qual o tipo de uso?'),
        vocabulary=vocabulary_1,
    )

    model.fieldset(
        'tab_c',
        label=_(u'Proposta'),
        fields=[
            'field_20',
            'field_21',
            'field_22',
            'field_23',
            'field_24',
            'field_25',
            'field_26',
            'field_27',
            'field_28',
        ],
    )

    field_20 = schema.Int(
        title=_(u'Custo total do projeto'),
    )

    field_21 = schema.Int(
        title=_(u'Duração'),
    )

    field_22 = schema.Text(
        title=_(u'Justificativa'),
    )

    field_23 = schema.Text(
        title=_(u'Memorial Descritivo'),
    )

    field_24 = schema.Choice(
        title=_(u'Material predominante na construção da plataforma'),
        vocabulary=vocabulary_2,
    )

    field_25 = schema.Int(
        title=_(u'Comprimento'),
    )

    field_26 = schema.Int(
        title=_(u'Largura'),
    )

    field_27 = schema.Int(
        title=_(u'Altura do Guarda Corpo'),
    )

    field_28 = schema.Text(
        title=_(u'Mobiliário urbano'),
    )

    model.fieldset(
        'tab_d',
        label=_(u'Anexos'),
        fields=[
            'file_1',
            'file_2',
            'file_3',
            'file_4',
            'file_5',
            'file_6',
            'file_7',
        ],
    )

    file_1 = NamedFile(
        title=_(u'Vista lateral esquerda'),
        required=False,
    )

    file_2 = NamedFile(
        title=_(u'Vista lateral direita'),
        required=False,
    )

    file_3 = NamedFile(
        title=_(u'Planta'),
        required=False,
    )

    file_4 = NamedFile(
        title=_(u'Cortes'),
        required=False,
    )

    file_5 = NamedFile(
        title=_(u'Memorial descritivo'),
        required=False,
    )

    file_6 = NamedFile(
        title=_(u'Planta inicial do local'),
        required=False,
    )

    file_7 = NamedFile(
        title=_(u'Planta proposta'),
        required=False,
    )

    model.fieldset(
        'tab_e',
        label=_(u'Resumo'),
        fields=['summary'],
    )

    summary = schema.Text(
        title=_(u'Resumo da proposta'),
    )


class ParkletForm(AutoExtensibleForm, EditForm):

    """Form handling."""

    schema = IParklet
    ignoreContext = True

    label = _(u'Cadastro Parklet')
    description = _(u'')

    def update(self):
        super(ParkletForm, self).update()
        self.request.set('disable_border', 1)  # hide the edit bar

    @button.buttonAndHandler(_(u'Ok'))
    def handleApply(self, action):
        data, errors = self.extractData()
        if not errors:
            self.status = self.formErrorsMessage
            return

        # Do something with valid data here
        # import pdb; pdb.set_trace()

        # Set status on this form page
        # (this status message is not bind to the session and does not go thru redirects)
        self.status = _(u'Cadastro efetuado com sucesso!')

    @button.buttonAndHandler(_(u'Cancelar'))
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page."""
