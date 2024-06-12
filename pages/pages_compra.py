from selenium import webdriver
from selenium.webdriver.common.by import By



class CargaPagina:
    """
    Clase que contiene los elementos de la pagina a utilizar para la compra y funcionalidades base para las pruebas
    """
    def __init__(self, driver: webdriver.Remote): #El método __init__ se llama automáticamente cuando se crea una nueva instancia de la clase.
        self.driver = driver


