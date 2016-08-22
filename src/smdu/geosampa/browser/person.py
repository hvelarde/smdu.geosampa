# -*- coding: utf-8 -*-
"""Formulário de cadastro de Pessoa jurídica."""
from plone.autoform.form import AutoExtensibleForm
from plone.formwidget.masterselect import MasterSelectField
from plone.supermodel import model
from smdu.geosampa import _
from z3c.form import button
from z3c.form.form import EditForm
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

person_type_vocab = SimpleVocabulary([
    SimpleTerm(value=u'fisica', title=_(u'Física')),
    SimpleTerm(value=u'juridica', title=_(u'Jurídica')),
])


class IPerson(model.Schema):

    """Form fields."""

    person_type = MasterSelectField(
        title=_(u'Tipo de pessoa'),
        vocabulary=person_type_vocab,
        slave_fields=(
            {
                'name': 'cnpj',
                'action': 'hide',
                'hide_values': ('fisica',),
                'siblings': True,
            },
            {
                'name': 'email',
                'action': 'hide',
                'hide_values': ('fisica',),
                'siblings': True,
            },
            {
                'name': 'phone',
                'action': 'hide',
                'hide_values': ('fisica',),
                'siblings': True,
            },
        ),
    )

    name = schema.TextLine(
        title=_(u'Name'),
    )

    rg = schema.ASCIILine(
        title=_(u'RG'),
    )

    cpf = schema.ASCIILine(
        title=_(u'CPF'),
    )

    cnpj = schema.ASCIILine(
        title=_(u'CNPJ'),
    )

    email = schema.ASCIILine(
        title=_(u'Email'),
    )

    phone = schema.ASCIILine(
        title=_(u'Phone'),
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


class PersonForm(AutoExtensibleForm, EditForm):

    """Form handling."""

    schema = IPerson
    ignoreContext = True

    label = _(u'Cadastro Pessoa')
    description = _(u'')

    def update(self):
        super(PersonForm, self).update()
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
        self.status = _('Cadastro efetuado com sucesso!')

    @button.buttonAndHandler(_(u'Cancelar'))
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page."""
