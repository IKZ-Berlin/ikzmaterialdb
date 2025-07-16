from nomad.config.models.plugins import SchemaPackageEntryPoint


class MaterialDbSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from ikzmaterialdb.schema_packages.schema import m_package

        return m_package


schema_package_entry_point = MaterialDbSchemaPackageEntryPoint(
    name='Material Database Schema Package',
    description='IKZ material database schema package entry point configuration.',
)
