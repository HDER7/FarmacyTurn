import unittest
import cambia_texto


class ProbrarCambiaTexto(unittest.TestCase):
    def test_mayuscula(self):
        palabra = 'buen dia'
        resultado = cambia_texto.mayus(palabra)
        self.assertEquals(resultado,'Buen Dia')


if __name__ == '__main__':
    unittest.main()