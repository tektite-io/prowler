from providers.aws.lib.audit_info.audit_info import current_audit_info
from providers.aws.services.shield.shield_service import Shield

shield_client = Shield(current_audit_info)
