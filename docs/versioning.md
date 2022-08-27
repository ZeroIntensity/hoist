# Version Garuntees

## API

Breaking API changes will only be included in new major versions (`X.x.x`), but features may be deprecated in new minor versions (`x.X.x`).

This means that 1.0.0 will have the same API as 1.5.0, but cannot be garunteed for 2.0.0.

## Server and Client

The Hoist protocol itself will be the same for major versions (ex. 1.0.0 will be able to properly work with 1.1.0)

However, operations will only be the same for **minor** versions (`x.X.x`), as long as the major version is the same (ex. 1.1.0 will include the same operations as 1.1.5)

## Patches

Patches, or micro versions (`x.x.X`) will not include any changes other than bug fixes.
