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

if __name__ == "__main__":
    unittest.main()
