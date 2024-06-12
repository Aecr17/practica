from selenium import webdriver
from selenium.webdriver.common.by import By

class AgregarProducto:
    """
    Clase que contiene los elementos para agregar un producto al carrito
    """
    def __init__(self, driver: webdriver.Remote): #El método __init__ se llama automáticamente cuando se crea una nueva instancia de la clase.
        self.driver = driver

    @property 
    def __aceptar_cookies(self):
     return self.driver.find_element(By.XPATH, "//a[@data-amplitude-event-name='cookie_banner_acknowledge_click']")
    
    @property
    def __agregar_carrito(self):
     return self.driver.find_element(By.CSS_SELECTOR, "input.js-addtocart.js-prod-submit-form.btn.btn-primary.btn-block.mb-4.cart[value='Agregar al carrito'][data-store='product-buy-button'][data-component='product.add-to-cart']")

 # Funciones que se interactuan con agregar un producto al carrito    
    def interactuar_cookies(self):
     """
     interactuar con la cookies que aparecen en la pagina
     """
     self.__aceptar_cookies.click()

    def agregar_producto(self):
     """
     Método que se encarga de agregar un producto al carrito
     """
     self.__agregar_carrito.click()