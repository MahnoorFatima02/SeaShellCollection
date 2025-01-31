template = {
    "swagger": "2.0",
    "info": {
        "title": "SeaShell API",
        "description": "API for managing seashell collections",
        "version": "1.0"
    },
    "paths": {
        "/api/shells": {
            "get": {
                "tags": ["Shells"],
                "summary": "Get all shells",
                "responses": {
                    "200": {
                        "description": "List of all shells"
                    }
                }
            },
            "post": {
                "tags": ["Shells"],
                "summary": "Create a new shell",
                "parameters": [{
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "species": {"type": "string"},
                            "description": {"type": "string"},
                            "location": {"type": "string"},
                            "size": {"type": "string"}
                        }
                    }
                }],
                "responses": {
                    "201": {
                        "description": "Shell created successfully"
                    }
                }
            }
        },
        "/api/shells/{id}": {
            "get": {
                "tags": ["Shells"],
                "summary": "Get a shell by ID",
                "parameters": [{
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "type": "integer"
                }],
                "responses": {
                    "200": {
                        "description": "Shell details"
                    }
                }
            },
            "put": {
                "tags": ["Shells"],
                "summary": "Update a shell",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "species": {"type": "string"},
                                "description": {"type": "string"},
                                "location": {"type": "string"},
                                "size": {"type": "string"}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Shell updated successfully"
                    }
                }
            },
            "delete": {
                "tags": ["Shells"],
                "summary": "Delete a shell",
                "parameters": [{
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "type": "integer"
                }],
                "responses": {
                    "204": {
                        "description": "Shell deleted successfully"
                    }
                }
            }
        }
    }
}
