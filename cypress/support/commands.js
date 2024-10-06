Cypress.Commands.add('getDataCy', (selector) => {
  return cy.get(`[data-cy=${selector}]`);
});