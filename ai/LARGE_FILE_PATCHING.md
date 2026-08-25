# U-GAS Large-File Safety

Treat large, append-only, truncated, generated, or structured files as unsafe to replace from a partial read. Inspect targeted ranges, use an existing repository patch mechanism where one exists, preserve unchanged bytes, and verify the resulting diff. If exact safe editing cannot be established, stop and report the boundary rather than reconstructing the file from incomplete context.
