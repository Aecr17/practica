from selenium import webdriver
from selenium.webdriver.common.by import By

class VerCarrito:
    """
    Metodo que contiene los elementos para mirar el carrito
    """
    def __init__(self, driver: webdriver.Remote): #El método __init__ se llama automáticamente cuando se crea una nueva instancia de la clase.
        self.driver = driver

    @property
    def __ver_carrito(self):
        return self.driver.find_element(By.ID, "a.js-modal-open.js-fullscreen-modal-open.btn.btn-link.ml-1.text-primary[data-toggle='#modal-cart'][data-modal-url='modal-fullscreen-cart']")
    
    def carrito_compras(self):
        """
        metodo para observar dentro del carrito
        """
        self.__ver_carrito.click()
        