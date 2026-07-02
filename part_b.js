import React, { useState } from "react";

function InvoiceList({ invoices }) {
  const [searchTerm, setSearchTerm] = useState("");
  
  // FIX 1 (Stale State / Lag): Removed the 'filtered' useState hook. 
  // Filtering state synchronously during render ensures the displayed list 
  // always perfectly matches the current searchTerm, eliminating the 1-keystroke lag.
  const filteredInvoices = invoices.filter((inv) =>
    inv.clientName.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search by client..."
        value={searchTerm}
        onChange={handleSearch}
      />
      <ul>
        {filteredInvoices.map((inv) => (
          /* FIX 2 (List Rendering): Added a unique 'key' prop to the mapped element */
          /* Assuming 'id' exists on the invoice object. If not, clientName could act as a fallback */
          <li key={inv.id || inv.clientName}>
            {inv.clientName} - ${inv.total}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default InvoiceList;
