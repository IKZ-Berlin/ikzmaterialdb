from nomad.config.models.plugins import SchemaPackageEntryPoint


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from ikzmaterialdb.schema_packages.schema import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='Material Database Schema Package',
    description='IKZ material database schema package entry point configuration.',
)
