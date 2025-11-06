# Premiers tests

On va chercher l'image chez Googlg User Content

<https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiODEvTzbXj7c-ktOe-d3F0GOqrJlw1LrNt8vUZWihYKb1eKK8oxYmfJgFsKh83DtJMIhYc3n-oc8s7LA1-aQNhOI-_i_w-zKovaI9LP1NYi6brVSpAr3VGDTH8hHmq43iR1GuZCK0u3mKoZL3O6-T1w_7w86awVn3mEzoyOlHgXgPFKY28dt67QGFxZ1fi/w640-h336/2025-04-18_10h43_0811.png>

- Image

![Téléchargez gratuitement](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiODEvTzbXj7c-ktOe-d3F0GOqrJlw1LrNt8vUZWihYKb1eKK8oxYmfJgFsKh83DtJMIhYc3n-oc8s7LA1-aQNhOI-_i_w-zKovaI9LP1NYi6brVSpAr3VGDTH8hHmq43iR1GuZCK0u3mKoZL3O6-T1w_7w86awVn3mEzoyOlHgXgPFKY28dt67QGFxZ1fi/w640-h336/2025-04-18_10h43_0811.png)

- Image avec lien url

[![Capture d'écran](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiODEvTzbXj7c-ktOe-d3F0GOqrJlw1LrNt8vUZWihYKb1eKK8oxYmfJgFsKh83DtJMIhYc3n-oc8s7LA1-aQNhOI-_i_w-zKovaI9LP1NYi6brVSpAr3VGDTH8hHmq43iR1GuZCK0u3mKoZL3O6-T1w_7w86awVn3mEzoyOlHgXgPFKY28dt67QGFxZ1fi/w640-h336/2025-04-18_10h43_0811.png)](https://www.trading-et-data-analyses.com/2025/11/migration-de-la-documentation-de.html)

- html copié directement depuis blogger

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><span style="margin-left: auto; margin-right: auto;"><a href="https://github.com/SoDevLog/PyTrading/releases" target="_blank"><img alt="TradingInPython - Plateforme de Trading en Python - Téléchargez gratuitement" border="0" data-original-height="336" data-original-width="639" height="336" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiODEvTzbXj7c-ktOe-d3F0GOqrJlw1LrNt8vUZWihYKb1eKK8oxYmfJgFsKh83DtJMIhYc3n-oc8s7LA1-aQNhOI-_i_w-zKovaI9LP1NYi6brVSpAr3VGDTH8hHmq43iR1GuZCK0u3mKoZL3O6-T1w_7w86awVn3mEzoyOlHgXgPFKY28dt67QGFxZ1fi/w640-h336/2025-04-18_10h43_0811.png" title="TradingInPython - Plateforme de Trading en Python - Téléchargez gratuitement" width="640" /></a></span></td></tr><tr><td class="tr-caption" style="text-align: center;"><a href="https://github.com/SoDevLog/PyTrading/releases" target="_blank">TradingInPython - Plateforme de Trading en Python - Téléchargez gratuitement</a></td></tr></tbody></table>

## Exemple d'image centrée

- css style **img.centered**

<p align="center">
  <img src="../images/trading_in_python.png" alt="Trading In Python" class="centered"/>
</p>

<p align="center">
  <img src="images/trading_in_python.png" alt="Trading In Python" class="centered"/>
</p>

- css class **noborder**

<p align="center">
  <img src="/images/trading_in_python.png" alt="Trading In Python" class="noborder"/>
</p>

### Description

img.noborder dans :

- \docs\css\extra.css

## Exemple avec sous-titre

**Noter le chemin relatif !!!!**

<figure style="text-align: center;">
  <img src="../images/trading_in_python.png" class="centered" width="600" />
  <figcaption><em>Figure 1 – Interface principale de l'application</em></figcaption>
</figure>

## Image cliquable

Chemin en relatif

<figure style="text-align: center;">
  <a href="../images/trading_in_python.png" target="_blank" title="Titre de l'image">
    <img src="../images/trading_in_python.png" alt="Capture d'écran" class="centered" width="450" />
  </a>
  <figcaption><em>Figure 1 – Cliquez pour agrandir</em></figcaption>
</figure>

Chemin en absolu

<figure style="text-align: center;">
  <a href="/images/trading_in_python.png" target="_blank" title="Titre de l'image">
    <img src="/images/trading_in_python.png" alt="Capture d'écran" class="centered" width="450" />
  </a>
  <figcaption><em>Figure 1 – Cliquez pour agrandir</em></figcaption>
</figure>

Noter le chemin utilise **{{ base_url }}**

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/trading_in_python.png" target="_blank" title="Titre de l'image">
    <img src="{{ base_url }}/images/trading_in_python.png" alt="Capture d'écran" class="centered" width="450" />
  </a>
  <figcaption><em>Figure 1 – Cliquez pour agrandir</em></figcaption>
</figure>

## Images glightbox

[Github glightbox](https://github.com/biati-digital/glightbox)

- Caroussel d'images
- Le comportement de la flèche du navigateur est différent

<a href="/images/trading_in_python.png" class="glightbox" data-gallery="galerie">
  <img src="/images/trading_in_python.png" alt="Image 1" width="200" />
</a>

<a href="/images/trading_in_python_2.png" class="glightbox" data-gallery="galerie">
  <img src="/images/trading_in_python_2.png" alt="Image 2" width="200" />
</a>
