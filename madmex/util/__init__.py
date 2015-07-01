'''
madmex.util

This package contains several useful classes and methods.
'''

def format_string(string, spaces, size):
    output = ""
    chunk = size - spaces - 2  
    output += space_string(spaces, " ") + "'"+string [0:chunk] + "'\n"
    indented_chunk = size - (spaces + 4) - 2
    for i in range (chunk, len(string), indented_chunk):
        output += space_string(spaces+4, " ") + "'"+string [i:i+indented_chunk] + "'\n"
    return output

def space_string(spaces, ch):
    output = ""
    i = 0
    while i < spaces:
        output += ch
        i+= 1
    return output

# a => \u00E1
# e => \u00E9
# i => \u00ED
# o => \u00F3
# u => \u00FA

if __name__ == "__main__":
    xml1 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>madmex_lcc_landsat_1993_v4</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap type="intervals"><sld:ColorMapEntry color="#FFFFFF" label=" " opacity="1.0" quantity="0"/><sld:ColorMapEntry color="#005500" label="Bosque De Coniferas" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#006C00" label="Bosque De Coniferas Herbacea" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#00CF98" label="Bosque De Encino-Pino Y Pino-Encino Herbacea" opacity="1.0" quantity="3"/><sld:ColorMapEntry color="#FFFF7F" label="Agricultura" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#E59900" label="Matorral Xerofilo Herbacea" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#AA55FF" label="Selvas Secas Arborea" opacity="1.0" quantity="6"/><sld:ColorMapEntry color="#008B00" label="Bosque De Coniferas Arborea" opacity="1.0" quantity="7"/><sld:ColorMapEntry color="#C7C8BC" label="Suelo Desnudo" opacity="1.0" quantity="8"/><sld:ColorMapEntry color="#AAFFFF" label="Vegetacion Hidrofila" opacity="1.0" quantity="9"/><sld:ColorMapEntry color="#AA007F" label="Selvas Secas" opacity="1.0" quantity="10"/><sld:ColorMapEntry color="#00AA00" label="Bosque De Encino " opacity="1.0" quantity="11"/><sld:ColorMapEntry color="#AA00FF" label="Selvas Secas Herbacea" opacity="1.0" quantity="12"/><sld:ColorMapEntry color="#00C100" label="Bosque De Encino Arborea" opacity="1.0" quantity="13"/><sld:ColorMapEntry color="#AAAA7F" label="Pastizales" opacity="1.0" quantity="14"/><sld:ColorMapEntry color="#FF00FF" label="Selvas Humedas Y Subhumedas Y Bosque Mesofilo Arborea" opacity="1.0" quantity="15"/><sld:ColorMapEntry color="#9F6A00" label="Matorral Xerofilo" opacity="1.0" quantity="16"/><sld:ColorMapEntry color="#00D800" label="Bosque De Encino Herbacea" opacity="1.0" quantity="17"/><sld:ColorMapEntry color="#000000" label="Urbano Y Construido" opacity="1.0" quantity="18"/><sld:ColorMapEntry color="#0000FF" label="Cuerpo De Agua" opacity="1.0" quantity="19"/><sld:ColorMapEntry color="#BD7E00" label="Matorral Xerofilo Arborea" opacity="1.0" quantity="20"/><sld:ColorMapEntry color="#00FFFF" label="Vegetacion Hidrofila Herbacea" opacity="1.0" quantity="21"/><sld:ColorMapEntry color="#00AA7F" label="Bosque De Encino-Pino Y Pino-Encino" opacity="1.0" quantity="22"/><sld:ColorMapEntry color="#FF007F" label="Selvas Humedas Y Subhumedas Y Bosque Mesofilo" opacity="1.0" quantity="23"/><sld:ColorMapEntry color="#00C893" label="Bosque De Encino-Pino Y Pino-Encino Arborea" opacity="1.0" quantity="24"/><sld:ColorMapEntry color="#B000B0" label="Selvas Humedas Y Subhumedas Y Bosque Mesofilo Herbacea" opacity="1.0" quantity="25"/><sld:ColorMapEntry color="#AAAA7F" label="Pastizales Herbacea" opacity="1.0" quantity="26"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'

    xml2 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>madmex_lcc_landsat_1993_v4</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap type="intervals"><sld:ColorMapEntry color="#75A8D4" label=" " opacity="1.0" quantity="0"/><sld:ColorMapEntry color="#006D00" label="Bosque de Ayarin; Cedro" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#00AA00" label="Bosque Encino(-Pino); Matorral Subtropical" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#005500" label="Bosque de Pino (-Encino); Abies; Oyamel; Tascate; Matorral de Coniferas" opacity="1.0" quantity="3"/><sld:ColorMapEntry color="#AAAA00" label="Matorral Submontano; Mequital Tropical; Bosque Mezquital" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#AA8000" label="Bosque de Mezquite; Matorral Desertico Microfilo; Mezquital Desertico; Vegetacion de Galeria" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#8BAA00" label="Chaparral" opacity="1.0" quantity="6"/><sld:ColorMapEntry color="#FF8000" label="Matorral Crasicaule" opacity="1.0" quantity="7"/><sld:ColorMapEntry color="#FF0000" label="Bosque Mesofilo de Montana; Selva Baja Perennifolio" opacity="1.0" quantity="8"/><sld:ColorMapEntry color="#AA007F" label="Selva Baja (Sub)Caducifolia; Espinosa (Caducifolia); Palmar Inducido" opacity="1.0" quantity="9"/><sld:ColorMapEntry color="#AA00FF" label="Selva Baja y Mediana (Espinosa) Subperennifolia; Selva de Galeria; Palmar Natural" opacity="1.0" quantity="10"/><sld:ColorMapEntry color="#FF007F" label="Selva Alta Subperennifolia" opacity="1.0" quantity="11"/><sld:ColorMapEntry color="#FF00FF" label="Selva Alta y Mediana Perennifolia" opacity="1.0" quantity="12"/><sld:ColorMapEntry color="#FF55FF" label="Selva Mediana (Sub) Caducifolia" opacity="1.0" quantity="13"/><sld:ColorMapEntry color="#AAFFFF" label="Tular" opacity="1.0" quantity="14"/><sld:ColorMapEntry color="#00FFFF" label="Popal" opacity="1.0" quantity="15"/><sld:ColorMapEntry color="#FFAAFF" label="Manglar; Vegetacion de Peten" opacity="1.0" quantity="16"/><sld:ColorMapEntry color="#E29700" label="Matorral Sarco-Crasicaule" opacity="1.0" quantity="17"/><sld:ColorMapEntry color="#BD7E00" label="Matorral Sarco-Crasicaule de Neblina" opacity="1.0" quantity="18"/><sld:ColorMapEntry color="#966400" label="Matorral Sarcocaule" opacity="1.0" quantity="19"/><sld:ColorMapEntry color="#75ECAF" label="Vegetacion de Dunas Costeras" opacity="1.0" quantity="20"/><sld:ColorMapEntry color="#C46200" label="Matorral Desertico Rosetofilo" opacity="1.0" quantity="21"/><sld:ColorMapEntry color="#AA5500" label="Matorral Espinosa Tamaulipeco" opacity="1.0" quantity="22"/><sld:ColorMapEntry color="#6D3600" label="Matorral Rosetofilo Costero" opacity="1.0" quantity="23"/><sld:ColorMapEntry color="#00AA7F" label="Vegetacion de Desiertos Arenos" opacity="1.0" quantity="24"/><sld:ColorMapEntry color="#008A65" label="Vegetacion Halofila Hidrofila" opacity="1.0" quantity="25"/><sld:ColorMapEntry color="#005941" label="Vegetacion Gipsofila Halofila Xerofila" opacity="1.0" quantity="26"/><sld:ColorMapEntry color="#AAAA7F" label="Pastizal y Sabana" opacity="1.0" quantity="27"/><sld:ColorMapEntry color="#FFFF7F" label="Agricultura" opacity="1.0" quantity="28"/><sld:ColorMapEntry color="#0000FF" label="Agua" opacity="1.0" quantity="29"/><sld:ColorMapEntry color="#C7C8BC" label="Sin y Desprovisto de Vegetacion" opacity="1.0" quantity="30"/><sld:ColorMapEntry color="#000000" label="Urbana" opacity="1.0" quantity="31"/><sld:ColorMapEntry color="#55AB00" label="Bosque Inducido; Cultivado; de Galeria" opacity="1.0" quantity="123"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'

    xml3 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>DF+Morelos</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap><sld:ColorMapEntry color="#84c96f" label="Bosque de Ayarin" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#63f73e" label="Bosque de Cedro" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#3cab32" label="Bosque de Oyamel" opacity="1.0" quantity="3"/><sld:ColorMapEntry color="#92a685" label="Bosque de Pino" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#cff7c6" label="Bosque de Tascate" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#88e04c" label="Bosque de Encino" opacity="1.0" quantity="6"/><sld:ColorMapEntry color="#7ca668" label="Bosque de Encino-Pino" opacity="1.0" quantity="7"/><sld:ColorMapEntry color="#91f27c" label="Bosque de Pino-Encino" opacity="1.0" quantity="8"/><sld:ColorMapEntry color="#bbf09e" label="Bosque cultivado" opacity="1.0" quantity="9"/><sld:ColorMapEntry color="#46c72c" label="Bosque inducido" opacity="1.0" quantity="10"/><sld:ColorMapEntry color="#ae3dd1" label="Bosque Mesofilo de Montana" opacity="1.0" quantity="11"/><sld:ColorMapEntry color="#dfb6e3" label="Selva Alta Perennifolia" opacity="1.0" quantity="12"/><sld:ColorMapEntry color="#e880e6" label="Selva Baja Perennifolia" opacity="1.0" quantity="13"/><sld:ColorMapEntry color="#a772b5" label="Selva Mediana Perennifolia" opacity="1.0" quantity="14"/><sld:ColorMapEntry color="#aa4fb8" label="Palmar natural" opacity="1.0" quantity="15"/><sld:ColorMapEntry color="#f23df2" label="Peten" opacity="1.0" quantity="16"/><sld:ColorMapEntry color="#f269f5" label="Selva da Galeria" opacity="1.0" quantity="17"/><sld:ColorMapEntry color="#e6a1f0" label="Selva Alta Subperennifolia" opacity="1.0" quantity="18"/><sld:ColorMapEntry color="#b58cb8" label="Selva Mediana Subperennifolia" opacity="1.0" quantity="19"/><sld:ColorMapEntry color="#c833f5" label="Selva Baja Espinosa Subperennifolia" opacity="1.0" quantity="20"/><sld:ColorMapEntry color="#ac63ba" label="Bosque de Galeria" opacity="1.0" quantity="21"/><sld:ColorMapEntry color="#d94ff7" label="Palmar" opacity="1.0" quantity="22"/><sld:ColorMapEntry color="#dc7afa" label="Palmar inducido" opacity="1.0" quantity="23"/><sld:ColorMapEntry color="#b944c2" label="Vegetaci\u00F3n de Peten" opacity="1.0" quantity="24"/><sld:ColorMapEntry color="#d132ce" label="Manglar" opacity="1.0" quantity="25"/><sld:ColorMapEntry color="#cb5ced" label="Selva Baja Caducifolia" opacity="1.0" quantity="26"/><sld:ColorMapEntry color="#c68fcf" label="Selva Mediana Caducifolia" opacity="1.0" quantity="27"/><sld:ColorMapEntry color="#cd62d1" label="Selva Baja Espinosa Caducifolia" opacity="1.0" quantity="28"/><sld:ColorMapEntry color="#d98eed" label="Selva Baja Subcaducifolia" opacity="1.0" quantity="29"/><sld:ColorMapEntry color="#c47acc" label="Selva Baja Espinosa" opacity="1.0" quantity="30"/><sld:ColorMapEntry color="#f250f0" label="Selva Mediana Subcaducifolia" opacity="1.0" quantity="31"/><sld:ColorMapEntry color="#f0c990" label="Matorral Desertico Rosetofilo" opacity="1.0" quantity="43"/><sld:ColorMapEntry color="#d18a5a" label="Matorral Desertico RosetofiloVegetaci\u00F3n de Galeria" opacity="1.0" quantity="52"/><sld:ColorMapEntry color="#c2b8cc" label="Pastizal Halofilo" opacity="1.0" quantity="54"/><sld:ColorMapEntry color="#4b494d" label="Pastizal Natural" opacity="1.0" quantity="55"/><sld:ColorMapEntry color="#837e87" label="Pradera de Alta montana" opacity="1.0" quantity="56"/><sld:ColorMapEntry color="#ebe4f2" label="Pastizal inducido" opacity="1.0" quantity="59"/><sld:ColorMapEntry color="#615c66" label="Pastizal Cultivado" opacity="1.0" quantity="62"/><sld:ColorMapEntry color="#2cd4c0" label="Vegetaci\u00F3n Halofila Hidrofila" opacity="1.0" quantity="65"/><sld:ColorMapEntry color="#ffff73" label="Agricultura de Humedad" opacity="1.0" quantity="66"/><sld:ColorMapEntry color="#a8a800" label="Agricultura de Riego" opacity="1.0" quantity="67"/><sld:ColorMapEntry color="#ffe173" label="Agricultura de Temporal" opacity="1.0" quantity="68"/><sld:ColorMapEntry color="#8289d9" label="Acuicola" opacity="1.0" quantity="69"/><sld:ColorMapEntry color="#3832ed" label="Agua" opacity="1.0" quantity="70"/><sld:ColorMapEntry color="#ff5500" label="Asentamientos Humanos" opacity="1.0" quantity="71"/><sld:ColorMapEntry color="#a80000" label="Zona Urbana" opacity="1.0" quantity="72"/><sld:ColorMapEntry color="#cccccc" label="Sin Vegetaci\u00F3n aparente" opacity="1.0" quantity="73"/><sld:ColorMapEntry color="#b2b2b2" label="Desprovisto de Vegetaci\u00F3n" opacity="1.0" quantity="74"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'

    xml4 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>DF+Morelos</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap><sld:ColorMapEntry color="#203c00" label="Bosque de Coniferas" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#46d836" label="Bosque de Encino" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#55aa7f" label="Bosque Mezclado" opacity="1.0" quantity="3"/><sld:ColorMapEntry color="#aa007f" label="Selvas Humedas y Subhumedas y Bosque Mesofilo" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#7d26cf" label="Selvas Secas" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#d2691e" label="Matorral Xerofilo Arbustivo" opacity="1.0" quantity="7"/><sld:ColorMapEntry color="#a5a581" label="Pastizales" opacity="1.0" quantity="8"/><sld:ColorMapEntry color="#f6e87e" label="Agricultura" opacity="1.0" quantity="10"/><sld:ColorMapEntry color="#0000ff" label="Agua" opacity="1.0" quantity="11"/><sld:ColorMapEntry color="#5c0000" label="Urbano y Construido" opacity="1.0" quantity="12"/><sld:ColorMapEntry color="#e0e0e0" label="Suelo Desnudo" opacity="1.0" quantity="13"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'

    xml5 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>DF+Morelos</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap><sld:ColorMapEntry color="#203c00" label="Tierras forestales" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#91916d" label="Praderas" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#f6e87e" label="Tierras de uso agricola" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#0000ff" label="Agua" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#5c0000" label="Asentamientos" opacity="1.0" quantity="6"/><sld:ColorMapEntry color="#e0e0e0" label="Otros" opacity="1.0" quantity="7"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'

    xml6 = 'styled_layer_descriptor\':\'<?xml version="1.0" ?><sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld"><sld:UserLayer><sld:LayerFeatureConstraints><sld:FeatureTypeConstraint/></sld:LayerFeatureConstraints><sld:UserStyle><sld:Name>madmex_lcc_landsat_2000_v4.2</sld:Name><sld:Title/><sld:FeatureTypeStyle><sld:Name/><sld:Rule><sld:RasterSymbolizer><sld:Geometry><ogc:PropertyName>grid</ogc:PropertyName></sld:Geometry><sld:Opacity>1</sld:Opacity><sld:ColorMap type="intervals"><sld:ColorMapEntry color="#75a8d4" label=" " opacity="1.0" quantity="0"/><sld:ColorMapEntry color="#005100" label="Bosque de Ayarin; Cedro" opacity="1.0" quantity="1"/><sld:ColorMapEntry color="#007e00" label="Bosque Encino(-Pino); Matorral Subtropical" opacity="1.0" quantity="2"/><sld:ColorMapEntry color="#003c00" label="Bosque de Pino (-Encino); Abies; Oyamel; Tascate; Matorral de Coniferas" opacity="1.0" quantity="3"/><sld:ColorMapEntry color="#aaaa00" label="Matorral Submontano; Mequital Tropical; Bosque Mezquital" opacity="1.0" quantity="4"/><sld:ColorMapEntry color="#aa8000" label="Bosque de Mezquite; Matorral Desertico Microfilo; Mezquital Desertico; Vegetacion de Galeria" opacity="1.0" quantity="5"/><sld:ColorMapEntry color="#8baa00" label="Chaparral" opacity="1.0" quantity="6"/><sld:ColorMapEntry color="#ffb265" label="Matorral Crasicaule" opacity="1.0" quantity="7"/><sld:ColorMapEntry color="#00d900" label="Bosque Mesofilo de Montana; Selva Baja Perennifolio" opacity="1.0" quantity="8"/><sld:ColorMapEntry color="#aa007f" label="Selva Baja (Sub)Caducifolia; Espinosa (Caducifolia); Palmar Inducido" opacity="1.0" quantity="9"/><sld:ColorMapEntry color="#ff55ff" label="Selva Baja y Mediana (Espinosa) Subperennifolia; Selva de Galeria; Palmar Natural" opacity="1.0" quantity="10"/><sld:ColorMapEntry color="#ff557f" label="Selva Alta Subperennifolia" opacity="1.0" quantity="11"/><sld:ColorMapEntry color="#ff007f" label="Selva Alta y Mediana Perennifolia" opacity="1.0" quantity="12"/><sld:ColorMapEntry color="#ff55ff" label="Selva Mediana (Sub) Caducifolia" opacity="1.0" quantity="13"/><sld:ColorMapEntry color="#aaffff" label="Tular" opacity="1.0" quantity="14"/><sld:ColorMapEntry color="#00ffff" label="Popal" opacity="1.0" quantity="15"/><sld:ColorMapEntry color="#55aaff" label="Manglar; Vegetacion de Peten" opacity="1.0" quantity="16"/><sld:ColorMapEntry color="#e29700" label="Matorral Sarco-Crasicaule" opacity="1.0" quantity="17"/><sld:ColorMapEntry color="#bd7e00" label="Matorral Sarco-Crasicaule de Neblina" opacity="1.0" quantity="18"/><sld:ColorMapEntry color="#966400" label="Matorral Sarcocaule" opacity="1.0" quantity="19"/><sld:ColorMapEntry color="#a2ecb1" label="Vegetacion de Dunas Costeras" opacity="1.0" quantity="20"/><sld:ColorMapEntry color="#c46200" label="Matorral Desertico Rosetofilo" opacity="1.0" quantity="21"/><sld:ColorMapEntry color="#aa5500" label="Matorral Espinosa Tamaulipeco" opacity="1.0" quantity="22"/><sld:ColorMapEntry color="#6d3600" label="Matorral Rosetofilo Costero" opacity="1.0" quantity="23"/><sld:ColorMapEntry color="#00aa7f" label="Vegetacion de Desiertos Arenos" opacity="1.0" quantity="24"/><sld:ColorMapEntry color="#008a65" label="Vegetacion Halofila Hidrofila" opacity="1.0" quantity="25"/><sld:ColorMapEntry color="#005941" label="Vegetacion Gipsofila Halofila Xerofila" opacity="1.0" quantity="26"/><sld:ColorMapEntry color="#e9e9af" label="Pastizal y Sabana" opacity="1.0" quantity="27"/><sld:ColorMapEntry color="#faff98" label="Agricultura" opacity="1.0" quantity="28"/><sld:ColorMapEntry color="#00007f" label="Agua" opacity="1.0" quantity="29"/><sld:ColorMapEntry color="#c7c8bc" label="Sin y Desprovisto de Vegetacion" opacity="1.0" quantity="30"/><sld:ColorMapEntry color="#4d1009" label="Urbana" opacity="1.0" quantity="31"/><sld:ColorMapEntry color="#6daa50" label="Bosque secondario" opacity="1.0" quantity="100"/><sld:ColorMapEntry color="#3a7500" label="Bosque Inducido; Cultivado; de Galeria" opacity="1.0" quantity="123"/><sld:ColorMapEntry color="#0b5923" label="Bosque de Pino-Encino; Matorral de Coniferas" opacity="1.0" quantity="124"/><sld:ColorMapEntry color="#ffaaff" label="Selva secundaria" opacity="1.0" quantity="200"/></sld:ColorMap></sld:RasterSymbolizer></sld:Rule></sld:FeatureTypeStyle></sld:UserStyle></sld:UserLayer></sld:StyledLayerDescriptor>'
    print format_string(xml1, 12, 80)