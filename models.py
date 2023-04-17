# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Property(models.Model):
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    area = models.IntegerField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    bedrooms = models.IntegerField(db_column='BEDROOMS', blank=True, null=True)  # Field name made lowercase.
    bathrooms = models.IntegerField(db_column='BATHROOMS', blank=True, null=True)  # Field name made lowercase.
    stories = models.IntegerField(db_column='STORIES', blank=True, null=True)  # Field name made lowercase.
    mainroad = models.CharField(db_column='MAINROAD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    guestroom = models.CharField(db_column='GUESTROOM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basement = models.CharField(db_column='BASEMENT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    hotwaterheating = models.CharField(db_column='HOTWATERHEATING', max_length=5, blank=True, null=True)  # Field name made lowercase.
    airconditioning = models.CharField(db_column='AIRCONDITIONING', max_length=5, blank=True, null=True)  # Field name made lowercase.
    parking = models.IntegerField(db_column='PARKING', blank=True, null=True)  # Field name made lowercase.
    prefarea = models.CharField(db_column='PREFAREA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    furnishingstatus = models.CharField(db_column='FURNISHINGSTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'property'


class PropertyProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    sqft = models.IntegerField()
    area = models.IntegerField(db_column='Area')  # Field name made lowercase.
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'property_product'


class PropertyUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    propertytransaction = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'property_user'


class Propertydata(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
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
