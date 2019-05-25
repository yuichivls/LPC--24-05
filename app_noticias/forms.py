from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=12)
    email = forms.EmailField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados = super().clean()
        # não aceita email do gmail
        email = dados.get('email', None)
        mensagem = dados.get('mensagem')
        if '@gmail.com' in email:
            self.add_error('email', 'Provedor de e-mail não suportado (gmail.com)')
            #testa palavras não permitidas na mensagem
            
        palavras = ['problema','defeito','erro']
        for palavra in palavras:
            if palavra in mensagem.lower():
                self.add_error('mensagem', 'O erro é teu otario')
        
        return dados