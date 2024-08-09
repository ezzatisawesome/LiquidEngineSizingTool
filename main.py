from InitialSizing import EngineSizer


test_engine = EngineSizer.Engine('config.yaml')
print(test_engine.design_isp)