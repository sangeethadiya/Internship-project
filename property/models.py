from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/property')
    price =models.IntegerField()
    sqft =models.IntegerField()
    Area =models.IntegerField()

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    propertytransaction=models.CharField(max_length=50)

    def __str__(self):
        return f'User:{self.first_name} {self.last_name}'

class BookForm(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    propertyid=models.IntegerField()
    propertytransaction=models.CharField(max_length=50)
  


class Propertydata(models.Model):
    mssubclass = models.IntegerField(db_column='MSSubClass', blank=True, null=True)  # Field name made lowercase.
    mszoning = models.TextField(db_column='MSZoning', blank=True, null=True)  # Field name made lowercase.
    lotfrontage = models.IntegerField(db_column='LotFrontage', blank=True, null=True)  # Field name made lowercase.
    lotarea = models.IntegerField(db_column='LotArea', blank=True, null=True)  # Field name made lowercase.
    street = models.TextField(db_column='Street', blank=True, null=True)  # Field name made lowercase.
    alley = models.TextField(db_column='Alley', blank=True, null=True)  # Field name made lowercase.
    lotshape = models.TextField(db_column='LotShape', blank=True, null=True)  # Field name made lowercase.
    landcontour = models.TextField(db_column='LandContour', blank=True, null=True)  # Field name made lowercase.
    utilities = models.TextField(db_column='Utilities', blank=True, null=True)  # Field name made lowercase.
    lotconfig = models.TextField(db_column='LotConfig', blank=True, null=True)  # Field name made lowercase.
    landslope = models.TextField(db_column='LandSlope', blank=True, null=True)  # Field name made lowercase.
    neighborhood = models.TextField(db_column='Neighborhood', blank=True, null=True)  # Field name made lowercase.
    condition1 = models.TextField(db_column='Condition1', blank=True, null=True)  # Field name made lowercase.
    condition2 = models.TextField(db_column='Condition2', blank=True, null=True)  # Field name made lowercase.
    bldgtype = models.TextField(db_column='BldgType', blank=True, null=True)  # Field name made lowercase.
    housestyle = models.TextField(db_column='HouseStyle', blank=True, null=True)  # Field name made lowercase.
    overallqual = models.IntegerField(db_column='OverallQual', blank=True, null=True)  # Field name made lowercase.
    overallcond = models.IntegerField(db_column='OverallCond', blank=True, null=True)  # Field name made lowercase.
    yearbuilt = models.IntegerField(db_column='YearBuilt', blank=True, null=True)  # Field name made lowercase.
    yearremodadd = models.IntegerField(db_column='YearRemodAdd', blank=True, null=True)  # Field name made lowercase.
    roofstyle = models.TextField(db_column='RoofStyle', blank=True, null=True)  # Field name made lowercase.
    roofmatl = models.TextField(db_column='RoofMatl', blank=True, null=True)  # Field name made lowercase.
    exterior1st = models.TextField(db_column='Exterior1st', blank=True, null=True)  # Field name made lowercase.
    exterior2nd = models.TextField(db_column='Exterior2nd', blank=True, null=True)  # Field name made lowercase.
    masvnrtype = models.TextField(db_column='MasVnrType', blank=True, null=True)  # Field name made lowercase.
    masvnrarea = models.IntegerField(db_column='MasVnrArea', blank=True, null=True)  # Field name made lowercase.
    exterqual = models.TextField(db_column='ExterQual', blank=True, null=True)  # Field name made lowercase.
    extercond = models.TextField(db_column='ExterCond', blank=True, null=True)  # Field name made lowercase.
    foundation = models.TextField(db_column='Foundation', blank=True, null=True)  # Field name made lowercase.
    bsmtqual = models.TextField(db_column='BsmtQual', blank=True, null=True)  # Field name made lowercase.
    bsmtcond = models.TextField(db_column='BsmtCond', blank=True, null=True)  # Field name made lowercase.
    bsmtexposure = models.TextField(db_column='BsmtExposure', blank=True, null=True)  # Field name made lowercase.
    bsmtfintype1 = models.TextField(db_column='BsmtFinType1', blank=True, null=True)  # Field name made lowercase.
    bsmtfinsf1 = models.IntegerField(db_column='BsmtFinSF1', blank=True, null=True)  # Field name made lowercase.
    bsmtfintype2 = models.TextField(db_column='BsmtFinType2', blank=True, null=True)  # Field name made lowercase.
    bsmtfinsf2 = models.IntegerField(db_column='BsmtFinSF2', blank=True, null=True)  # Field name made lowercase.
    bsmtunfsf = models.IntegerField(db_column='BsmtUnfSF', blank=True, null=True)  # Field name made lowercase.
    totalbsmtsf = models.IntegerField(db_column='TotalBsmtSF', blank=True, null=True)  # Field name made lowercase.
    heating = models.TextField(db_column='Heating', blank=True, null=True)  # Field name made lowercase.
    heatingqc = models.TextField(db_column='HeatingQC', blank=True, null=True)  # Field name made lowercase.
    centralair = models.TextField(db_column='CentralAir', blank=True, null=True)  # Field name made lowercase.
    electrical = models.TextField(db_column='Electrical', blank=True, null=True)  # Field name made lowercase.
    number_1stflrsf = models.IntegerField(db_column='1stFlrSF', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndflrsf = models.IntegerField(db_column='2ndFlrSF', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    lowqualfinsf = models.IntegerField(db_column='LowQualFinSF', blank=True, null=True)  # Field name made lowercase.
    grlivarea = models.IntegerField(db_column='GrLivArea', blank=True, null=True)  # Field name made lowercase.
    bsmtfullbath = models.IntegerField(db_column='BsmtFullBath', blank=True, null=True)  # Field name made lowercase.
    bsmthalfbath = models.IntegerField(db_column='BsmtHalfBath', blank=True, null=True)  # Field name made lowercase.
    fullbath = models.IntegerField(db_column='FullBath', blank=True, null=True)  # Field name made lowercase.
    halfbath = models.IntegerField(db_column='HalfBath', blank=True, null=True)  # Field name made lowercase.
    bedroomabvgr = models.IntegerField(db_column='BedroomAbvGr', blank=True, null=True)  # Field name made lowercase.
    kitchenabvgr = models.IntegerField(db_column='KitchenAbvGr', blank=True, null=True)  # Field name made lowercase.
    kitchenqual = models.TextField(db_column='KitchenQual', blank=True, null=True)  # Field name made lowercase.
    totrmsabvgrd = models.IntegerField(db_column='TotRmsAbvGrd', blank=True, null=True)  # Field name made lowercase.
    functional = models.TextField(db_column='Functional', blank=True, null=True)  # Field name made lowercase.
    fireplaces = models.IntegerField(db_column='Fireplaces', blank=True, null=True)  # Field name made lowercase.
    fireplacequ = models.TextField(db_column='FireplaceQu', blank=True, null=True)  # Field name made lowercase.
    garagetype = models.TextField(db_column='GarageType', blank=True, null=True)  # Field name made lowercase.
    garageyrblt = models.IntegerField(db_column='GarageYrBlt', blank=True, null=True)  # Field name made lowercase.
    garagefinish = models.TextField(db_column='GarageFinish', blank=True, null=True)  # Field name made lowercase.
    garagecars = models.IntegerField(db_column='GarageCars', blank=True, null=True)  # Field name made lowercase.
    garagearea = models.IntegerField(db_column='GarageArea', blank=True, null=True)  # Field name made lowercase.
    garagequal = models.TextField(db_column='GarageQual', blank=True, null=True)  # Field name made lowercase.
    garagecond = models.TextField(db_column='GarageCond', blank=True, null=True)  # Field name made lowercase.
    paveddrive = models.TextField(db_column='PavedDrive', blank=True, null=True)  # Field name made lowercase.
    wooddecksf = models.IntegerField(db_column='WoodDeckSF', blank=True, null=True)  # Field name made lowercase.
    openporchsf = models.IntegerField(db_column='OpenPorchSF', blank=True, null=True)  # Field name made lowercase.
    enclosedporch = models.IntegerField(db_column='EnclosedPorch', blank=True, null=True)  # Field name made lowercase.
    number_3ssnporch = models.IntegerField(db_column='3SsnPorch', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    screenporch = models.IntegerField(db_column='ScreenPorch', blank=True, null=True)  # Field name made lowercase.
    poolarea = models.IntegerField(db_column='PoolArea', blank=True, null=True)  # Field name made lowercase.
    poolqc = models.TextField(db_column='PoolQC', blank=True, null=True)  # Field name made lowercase.
    fence = models.TextField(db_column='Fence', blank=True, null=True)  # Field name made lowercase.
    miscfeature = models.TextField(db_column='MiscFeature', blank=True, null=True)  # Field name made lowercase.
    miscval = models.IntegerField(db_column='MiscVal', blank=True, null=True)  # Field name made lowercase.
    mosold = models.IntegerField(db_column='MoSold', blank=True, null=True)  # Field name made lowercase.
    yrsold = models.IntegerField(db_column='YrSold', blank=True, null=True)  # Field name made lowercase.
    saletype = models.TextField(db_column='SaleType', blank=True, null=True)  # Field name made lowercase.
    salecondition = models.TextField(db_column='SaleCondition', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.IntegerField(db_column='SalePrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertydata'
