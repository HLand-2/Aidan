def copy_instance_data(source, target):
    """Copies all instance attributes from source to target."""
    for key, value in vars(source).items():
        setattr(target, key, value)
