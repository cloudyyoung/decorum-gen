from models.object import *
from models.paint import *

# Initialize 4 for each object

object_classes = [
    RedModernWallHanging,
    RedUnusualCurio,
    RedRetroLamp,
    YellowUnsualWallHanging,
    YellowRetroCurio,
    YellowAntiqueLamp,
    BlueRetroWallHanging,
    BlueAntiqueCurio,
    BlueModernLamp,
    GreenAntiqueWallHanging,
    GreenModernCurio,
    GreenUnusualLamp,
]
objects = [cls() for cls in object_classes]

# Initialize 4 for each paint
paint_classes = [
    RedPaint,
    YellowPaint,
    BluePaint,
    GreenPaint,
]

paints = [cls() for cls in paint_classes]
