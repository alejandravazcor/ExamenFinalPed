import unittest
import protocolo

class TestRespuestaFrase(unittest.TestCase):
    def setUp(self):
        self.frases = ["Frase uno", "Frase dos"]
        self.lineas = 5

    def test_respuesta_empieza_por_frase(self):
        r = protocolo.generar_respuesta("frase", self.frases, self.lineas)
        self.assertTrue(r.startswith("frase "))

    def test_frase_devuelta_es_del_fichero(self):
        r = protocolo.generar_respuesta("frase", self.frases, self.lineas)
        texto = r[len("frase "):]
        self.assertIn(texto, self.frases)

class TestRespuestaTotal(unittest.TestCase):
    def setUp(self):
        self.frases = ["Frase uno", "Frase dos", "Frase tres"]
        self.lineas = 7

    def test_formato_total(self):
        r = protocolo.generar_respuesta("total", self.frases, self.lineas)
        self.assertEqual(r, "3 FRASES 7 LINEAS")

if __name__ == "__main__":
    unittest.main()
