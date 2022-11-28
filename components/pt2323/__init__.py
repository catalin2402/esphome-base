import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

DEPENDENCIES = ['i2c']

pt2323_ns = cg.esphome_ns.namespace('pt2323')
PT2323 = pt2323_ns.class_('PT2323', cg.Component,  i2c.I2CDevice)

CONF_PT2323_ID = 'pt2323_id'
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(PT2323),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x4A))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await i2c.register_i2c_device(var, config)
