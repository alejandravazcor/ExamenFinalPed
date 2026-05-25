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

class TestRespuestaError(unittest.TestCase):
    def setUp(self):
        self.frases = ["Una frase"]
        self.lineas = 1

    def test_comando_desconocido_devuelve_error(self):
        r = protocolo.generar_respuesta("hola", self.frases, self.lineas)
        self.assertEqual(r, "error")

    def test_construir_mensaje_codifica_utf8(self):
        resultado = protocolo.construir_mensaje("frase")
        self.assertEqual(resultado, b"frase\n")

class TestCargarFichero(unittest.TestCase):

    def test_carga_frases_del_fichero(self):
        frases = protocolo.cargar_fichero("frases")
        self.assertGreater(len(frases), 0)

    def test_cada_frase_no_es_separador(self):
        frases = protocolo.cargar_fichero("frases")
        for f in frases:
            self.assertNotEqual(f.strip(), "%")

    def test_contar_lineas_fichero(self):
        n = protocolo.contar_lineas_fichero("frases")
        self.assertGreater(n, 0)

if __name__ == "__main__":
    unittest.main()
