# -*- coding: utf-8 -*-
"""Formulário de cadastro de Área verde."""
from plone.autoform import directives as form
from plone.autoform.form import AutoExtensibleForm
from plone.formwidget.geolocation.field import GeolocationField
from plone.formwidget.masterselect import MasterSelectField
from plone.namedfile.field import NamedFile
from plone.supermodel import model
from smdu.geosampa import _
from z3c.form import button
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.form import EditForm
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

vocabulary_1 = SimpleVocabulary([
    SimpleTerm(value=u'manutencao', title=_(u'Manutenção e zeladoria')),
    SimpleTerm(value=u'melhorias', title=_(u'Melhorias Urbanísticas')),
    SimpleTerm(value=u'outros', title=_(u'Outros serviços/ Atividades')),
])

vocabulary_2 = SimpleVocabulary([
    SimpleTerm(value=u'21', title=_(u'Diária')),
    SimpleTerm(value=u'22', title=_(u'Semanal')),
    SimpleTerm(value=u'23', title=_(u'Mensal')),
    SimpleTerm(value=u'24', title=_(u'Bimestral')),
    SimpleTerm(value=u'25', title=_(u'Outra')),
])

vocabulary_3 = SimpleVocabulary([
    SimpleTerm(value=u'31', title=_(u'Arquitetônico')),
    SimpleTerm(value=u'32', title=_(u'Paisagístico')),
    SimpleTerm(value=u'33', title=_(u'Outros')),
])

vocabulary_4 = SimpleVocabulary([
    SimpleTerm(value=u'41', title=_(u'Restauro')),
    SimpleTerm(value=u'42', title=_(u'Arquitetônica')),
    SimpleTerm(value=u'43', title=_(u'Acessibilidade')),
    SimpleTerm(value=u'44', title=_(u'Paisagismo')),
    SimpleTerm(value=u'45', title=_(u'Mobilidade urbana')),
    SimpleTerm(value=u'46', title=_(u'Outros')),
])

vocabulary_5 = SimpleVocabulary([
    SimpleTerm(value=u'51', title=_(u'Banco')),
    SimpleTerm(value=u'52', title=_(u'Mesa')),
    SimpleTerm(value=u'53', title=_(u'Lixeira')),
    SimpleTerm(value=u'54', title=_(u'Brinquedos')),
    SimpleTerm(value=u'55', title=_(u'Equipamento de ginástica')),
    SimpleTerm(value=u'56', title=_(u'Horta')),
    SimpleTerm(value=u'57', title=_(u'Outros')),
])

vocabulary_6 = SimpleVocabulary([
    SimpleTerm(value=u'61', title=_(u'Apresentação')),
    SimpleTerm(value=u'62', title=_(u'Exposições/Feiras de artesanato')),
    SimpleTerm(value=u'63', title=_(u'Exibições (filmes) (Periodicidade: Semanal)')),
    SimpleTerm(value=u'64', title=_(u'Cursos livres/Oficinas')),
    SimpleTerm(value=u'65', title=_(u'Atividades de educação ambiental (Periodicidade: Mensal)')),
    SimpleTerm(value=u'66', title=_(u'Outros')),
])


class IGreenArea(model.Schema):

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
        fields=['field_1'],
    )

    field_1 = schema.Text(
        title=_(u'Mobiliário urbano'),
    )

    model.fieldset(
        'tab_c',
        label=_(u'Proposta'),
        fields=[
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
        ],
    )

    field_2 = MasterSelectField(
        title=_(u'Objeto da cooperação'),
        vocabulary=vocabulary_1,
        slave_fields=(
            {
                'name': 'field_3',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_4',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_5',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_6',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_7',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_8',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_9',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_10',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_11',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_12',
                'action': 'hide',
                'hide_values': ('melhorias', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_13',
                'action': 'hide',
                'hide_values': ('manutencao', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_14',
                'action': 'hide',
                'hide_values': ('manutencao', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_15',
                'action': 'hide',
                'hide_values': ('manutencao', 'outros'),
                'siblings': True,
            },
            {
                'name': 'field_16',
                'action': 'hide',
                'hide_values': ('manutencao', 'melhorias'),
                'siblings': True,
            },
            {
                'name': 'field_17',
                'action': 'hide',
                'hide_values': ('manutencao', 'melhorias'),
                'siblings': True,
            },
            {
                'name': 'field_18',
                'action': 'hide',
                'hide_values': ('manutencao', 'melhorias'),
                'siblings': True,
            },
        ),
    )

    field_3 = schema.Bool(
        title=_(u'Coleta de resíduos'),
    )

    field_4 = schema.Choice(
        title=_(u'Periodicidade'),
        vocabulary=vocabulary_2,
    )

    field_5 = schema.Bool(
        title=_(u'Manutenção de corte de grama'),
    )

    field_6 = schema.Bool(
        title=_(u'Manutenção de vegetação (não grama)'),
    )

    field_7 = schema.Bool(
        title=_(u'Varrição (Periodicidade: Diária)'),
    )

    field_8 = schema.Bool(
        title=_(u'Elementos construídos'),
    )

    field_9 = schema.Bool(
        title=_(u'Manutenção de mobiliário (Periodicidade: Mensal)'),
    )

    field_10 = schema.Bool(
        title=_(u'Outros'),
    )

    field_11 = schema.TextLine(
        title=_(u'Especifique'),
        required=False,
    )

    field_12 = schema.Choice(
        title=_(u'Periodicidade'),
        vocabulary=vocabulary_2,
    )

    form.widget('field_13', CheckBoxFieldWidget)
    field_13 = schema.Choice(
        title=_(u'Elaboração de projeto'),
        required=False,
        vocabulary=vocabulary_3,
    )

    form.widget('field_14', CheckBoxFieldWidget)
    field_14 = schema.Choice(
        title=_(u'Execução de obras'),
        required=False,
        vocabulary=vocabulary_4,
    )

    form.widget('field_15', CheckBoxFieldWidget)
    field_15 = schema.Choice(
        title=_(u'Instalação de mobiliário'),
        required=False,
        vocabulary=vocabulary_5,
    )

    form.widget('field_16', CheckBoxFieldWidget)
    field_16 = schema.Choice(
        title=_(u'Outros serviços/ Atividades'),
        vocabulary=vocabulary_6,
    )

    field_17 = schema.TextLine(
        title=_(u'Especifique'),
        required=False,
    )

    field_18 = schema.Choice(
        title=_(u'Periodicidade'),
        vocabulary=vocabulary_2,
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


class GreenAreaForm(AutoExtensibleForm, EditForm):

    """Form handling."""

    schema = IGreenArea
    ignoreContext = True

    label = _(u'Cadastro Área Verde')
    description = _(u'')

    def update(self):
        super(GreenAreaForm, self).update()
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
