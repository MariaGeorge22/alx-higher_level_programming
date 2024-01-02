#include "lists.h"
#include <stdlib.h>

/*
 * Function: check_cycle
 *
 * @check_cycle = Detects whether a linked list contains a cycle.
 *
 * Description: A pointer to the head of the linked list to be checked.
 *
 * Returns:
 * 1 if a cycle is found, 0 otherwise.
*/

int check_cycle(listint_t *list)
{
listint_t *prev = NULL;
listint_t *curr = NULL;

if (list == NULL)
{
return (0);
}

prev = list;
curr = list->next;

while (curr != NULL)
{
if (curr == prev)
{
return (1);
}
prev = prev->next;
curr = curr->next;
if (curr != NULL)
{
curr = curr->next;
}
}

return (0);
}
