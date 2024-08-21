from fastapi import APIRouter

router = APIRouter()

products_lists = ["Producto1", "Producto2", "Producto3", "Producto4", "Producto5"]

@router.get("/products")
async def products():
    return products_lists
